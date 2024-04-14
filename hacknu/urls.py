
from .views import QuizViewSet, QuizInstanceViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'quiz', QuizViewSet)
router.register(r'quiz_res', QuizInstanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]