from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Item, ItemCategory
from authentication.models import User

class UserNestedSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'avatar_url', 'telegram_url')
class ItemSerializer(ModelSerializer):
    user = UserNestedSerializer()
    created_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = Item
        fields = '__all__'

class ItemCategorySerializer(ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'