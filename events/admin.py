from django.contrib import admin

from .models import Club, EventCategory, Event
# Register your models here.

class EventInline(admin.TabularInline):
    model = Event


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    inlines = [EventInline]



@admin.register(EventCategory)
class eventCategoryAdmin(admin.ModelAdmin):
    inlines = [EventInline]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass