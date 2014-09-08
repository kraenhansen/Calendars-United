from django.contrib import admin
from feed_management.models import IngoingFeed, OutgoingFeed, FeedMapping

class IngoingFeedAdmin(admin.ModelAdmin):
    pass

admin.site.register(IngoingFeed, IngoingFeedAdmin)

class OutgoingFeedAdmin(admin.ModelAdmin):
    pass

admin.site.register(OutgoingFeed, OutgoingFeedAdmin)

class FeedMappingAdmin(admin.ModelAdmin):
    pass

admin.site.register(FeedMapping, FeedMappingAdmin)