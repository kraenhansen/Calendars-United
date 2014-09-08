from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from icalendar import Calendar, Event
from requests import get

from django.conf import settings

def set_or_is_equal(obj, key, value):
	if key in obj.keys():
		if str(obj[key]) == str(value):
			return True
		else:
			return False
	else:
		obj[key] = value
		return True

TRANSFER_CALENDAR_KEYS = [
	'CALSCALE',
	'X-WR-TIMEZONE',
	'METHOD'
]

def unite_calendars( urls ):
	united_calendar = Calendar()
	united_calendar['PRODID'] = settings.PRODID
	for url in urls:
		feed_response = get(url)
		if feed_response.status_code == 200:
			feed_content = feed_response.text
			feed_calendar = Calendar.from_ical(feed_content)
			# Transfer fields
			for (key, value) in feed_calendar.items():
				if key in TRANSFER_CALENDAR_KEYS:
					success = set_or_is_equal(united_calendar, key, value)
					if not success:
						raise BaseException("Can only unite calendars with the same values in the %s field, got %s and the calendar had %s" % (key, value, united_calendar[key]))
			# Transfer events and other
			for subcomponent in feed_calendar.subcomponents:
				united_calendar.add_component(subcomponent)
	return united_calendar

def unite(request):
	print(request.GET.keys())
	if "url[]" in request.GET.keys():
		urls = request.GET.getlist("url[]")
		united_calendar = unite_calendars( urls )
		united_calendar['X-WR-CALNAME'] = "United Calendar"
		united_calendar['X-WR-CALDESC'] = "A calendar united by the Calendars United system."
		response = HttpResponse( united_calendar.to_ical() )
		response["Cache-Control"] = "no-cache, no-store, max-age=0, must-revalidate"
		#response["Content-Type"] = "text/calendar; charset=UTF-8"
		response["Server"] = "Calendars-United-%s" % settings.VERSION
		return response
	else:
		return HttpResponseBadRequest("Use this with multiple url keys in the query string.")