from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import feed_management.urls, calendar_unitor.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'calendars_united.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(feed_management.urls)),
    url(r'^unitor/', include(calendar_unitor.urls)),
)
