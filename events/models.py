from django.db import models

from authentication.models import User

# Create your models here.

class Club(models.Model):
    members = models.ManyToManyField(User, related_name='clubs')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.name


class EventCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True, related_name='events')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='events')
    image_url = models.FileField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name