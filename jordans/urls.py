from django.urls import path
from .views import (
    JordanListView,
    JordanDetailView,
    JordanLikeView
)

urlpatterns = [
    path('', JordanListView.as_view()),
    path('<int:pk>/', JordanDetailView.as_view()),
    path('<int:jordan_pk>/like/', JordanLikeView.as_view())
]
