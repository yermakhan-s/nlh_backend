from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Vacancy, VacancyCategory
from authentication.models import User

class UserNestedSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'avatar_url', 'telegram_url')
class VacancySerializer(ModelSerializer):
    user = UserNestedSerializer()
    created_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = Vacancy
        fields = '__all__'

class VacancyCategorySerializer(ModelSerializer):
    class Meta:
        model = VacancyCategory
        fields = '__all__'