from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from feed_management.models import IngoingFeed, OutgoingFeed, FeedMapping
from calendar_unitor.views import unite_calendars
from django.conf import settings

def outgoing_feed(request, secret):
	outgoing_feed = OutgoingFeed.objects.get(secret_uuid = secret)
	urls = []
	for feed in outgoing_feed.mappings.all():
		urls.append(feed.ingoing.url)
	united_calendar = unite_calendars( urls )
	united_calendar['X-WR-CALNAME'] = "United Calendar"
	united_calendar['X-WR-CALDESC'] = "A calendar united by the Calendars United system."
	response = HttpResponse( united_calendar.to_ical() )
	response["Cache-Control"] = "no-cache, no-store, max-age=0, must-revalidate"
	response["Content-Type"] = "text/calendar; charset=UTF-8"
	response["Server"] = "Calendars-United-%s" % settings.VERSION
	return response

@login_required
def overview(request):
	ingoing_feeds = IngoingFeed.objects.filter(owner = request.user)
	outgoing_feeds = OutgoingFeed.objects.filter(owner = request.user)
	feed_mappings = FeedMapping.objects.filter(creator = request.user)
	return render(request, "feed_management/overview.html", {
		'ingoing_feeds': ingoing_feeds,
		'outgoing_feeds': outgoing_feeds,
		'feed_mappings': feed_mappings,
		})
	#return HttpResponse("Yay!")