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

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    authentication_classes = [JWTAuthentication]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields=['category_id', 'club_id', 'date']
    search_fields = ['name', 'description']

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Event.objects.all()
        date = self.request.query_params.get('date')
        if date is not None:
            queryset = queryset.filter(date__date=date)
        return queryset

    @action(methods=['get'], detail=False)
    def get_event_categories(self, request, *args, **kwargs):
        categories = EventCategory.objects.all()
        serializer = EventCategorySerializer(categories, many=True)
        return Response(serializer.data)

class ClubViewSet(ModelViewSet):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()
    authentication_classes = [JWTAuthentication]
