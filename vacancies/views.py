from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Vacancy, VacancyCategory
from .serializers import VacancySerializer, VacancyCategorySerializer
from rest_framework.decorators import action
from authentication.authentication import JWTAuthentication

class VacancyViewSet(ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
    authentication_classes = [JWTAuthentication]
    filterset_fields=['category_id', 'user_id']
    @action(methods=['get'], detail=False)
    def get_vacancy_categories(self, request, *args, **kwargs):
        categories = VacancyCategory.objects.all()
        serializer = VacancyCategorySerializer(categories, many=True)
        return Response(serializer.data)