from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Event, EventCategory, Club
from .serializers import EventSerializer, EventCategorySerializer, ClubSerializer
from rest_framework.decorators import action
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from datetime import datetime
from authentication.authentication import JWTAuthentication
from datetime import datetime

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    authentication_classes = [JWTAuthentication]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields=['category_id', 'club_id', 'date__date']
    search_fields = ['name', 'description']

    def get_queryset(self):
        queryset = Event.objects.all()
        date_str = self.request.query_params.get('date')
        if date_str is not None:
            queryset = queryset.filter(date__date=date_str)
        return queryset

    @action(methods=['get'], detail=False)
    def get_event_categories(self, request, *args, **kwargs):
        categories = EventCategory.objects.all()
        serializer = EventCategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def get_event_count_by_date(self, request, *args, **kwargs):
        events_by_date = Event.objects.values('date__date').annotate(count=Count('id'))
        event_count_by_date = {}
        for event in events_by_date:
            date_str = event['date__date'].strftime('%Y-%m-%d')
            event_count_by_date[date_str] = event['count']
        return Response(event_count_by_date)

class ClubViewSet(ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    authentication_classes = [JWTAuthentication]
