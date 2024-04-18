from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ClubViewSet

router = DefaultRouter()

router.register(r'^event', EventViewSet)
router.register(r'^club', ClubViewSet)