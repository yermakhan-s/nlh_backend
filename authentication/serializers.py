from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User


class UserSerializer(ModelSerializer):
    avatar_url = serializers.SerializerMethodField('get_avatar')

    def get_avatar(self, obj):
        if obj.avatar_url:
            return self.context['request'].build_absolute_uri(obj.avatar_url.url)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password', 'telegram_url', 'avatar_url', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserViewSetSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'telegram_url', 'avatar_url', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'id':{'read_only': True}
        }