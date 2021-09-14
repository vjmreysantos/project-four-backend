from django.urls import path
from .views import (
  RegisterView, LoginView, ProfileView, ProfileDetailView, ProfileListView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('users/', ProfileListView.as_view()),
    path('myprofile/', ProfileView.as_view()),
    path('profile/<username>/', ProfileDetailView.as_view())
]
