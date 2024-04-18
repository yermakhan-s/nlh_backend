from django.contrib import admin

from .models import Club, EventCategory, Event
# Register your models here.


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    pass


@admin.register(EventCategory)
class eventCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass