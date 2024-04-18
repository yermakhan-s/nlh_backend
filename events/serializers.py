from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Event, EventCategory, Club

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventCategorySerializer(ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'

class ClubSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'