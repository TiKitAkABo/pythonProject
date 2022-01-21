from django.urls import path, include
from .views import UserProfileListCreateView, userProfileDetailView


urlpatterns = [
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),#ссылка на создыние профиля
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),#ссылка на сам профиль с id
]