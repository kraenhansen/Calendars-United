from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^unite$', 'calendar_unitor.views.unite', name='unite'),
)
