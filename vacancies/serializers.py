from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Vacancy, VacancyCategory

class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

class VacancyCategorySerializer(ModelSerializer):
    class Meta:
        model = VacancyCategory
        fields = '__all__'