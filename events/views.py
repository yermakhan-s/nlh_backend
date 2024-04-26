from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Event, EventCategory, Club
from .serializers import EventSerializer, EventCategorySerializer, ClubSerializer
from rest_framework.decorators import action
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from authentication.authentication import JWTAuthentication
from datetime import datetime

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    authentication_classes = [JWTAuthentication]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields=['category_id', 'club_id', 'date__date']
    search_fields = ['name', 'description']

    @action(methods=['get'], detail=False)
    def get_event_categories(self, request, *args, **kwargs):
        categories = EventCategory.objects.all()
        serializer = EventCategorySerializer(categories, many=True)
        return Response(serializer.data)

class ClubViewSet(ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    authentication_classes = [JWTAuthentication]
