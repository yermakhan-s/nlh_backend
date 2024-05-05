from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer, SerializerMethodField

from .models import Event, EventCategory, Club


class ClubSerializer(ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class ClubNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'image_url') 
class EventSerializer(ModelSerializer):
    club = ClubNestedSerializer(required=False)
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M', required=False)
    created_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class EventCategorySerializer(ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'
