from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (confirmAttendanceAPIView, EventListCreateAPIView,)

router = DefaultRouter()
router.register("all-events", EventListCreateAPIView, basename='all-events')
router.register("confirm-attendance", confirmAttendanceAPIView)


urlpatterns = [
    path("", include(router.urls))
]