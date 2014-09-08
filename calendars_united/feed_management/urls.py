from django.conf.urls import patterns, include, url
from feed_management.forms import CustomAuthenticationForm

# print( CustomAuthenticationForm.fields )

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'feed_management.views.overview', name='overview'),
    url(r'^outgoing/(?P<secret>[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12})/$', 'feed_management.views.outgoing_feed', name='outgoing_feed'),
    url(r'^sign-in/$', 'django.contrib.auth.views.login', {
    	'template_name': 'feed_management/sign-in.html',
    	'authentication_form': CustomAuthenticationForm
    	}, name='sign-in'),
    url(r'^sign-out/$', 'django.contrib.auth.views.logout', name='sign-out'),
)
