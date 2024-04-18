from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Item, ItemCategory

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemCategorySerializer(ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'