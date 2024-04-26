from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Item, ItemCategory
from .serializers import ItemSerializer, ItemCategorySerializer
from rest_framework.decorators import action
from rest_framework import filters
from authentication.authentication import JWTAuthentication

class ItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    authentication_classes = [JWTAuthentication]
    filterset_fields=['category_id', 'user_id']
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    @action(methods=['get'], detail=False)
    def get_item_categories(self, request, *args, **kwargs):
        categories = ItemCategory.objects.all()
        serializer = ItemCategorySerializer(categories, many=True)
        return Response(serializer.data)