from django.urls import path
from .views import JordanListView, JordanDetailView

urlpatterns = [
    path('', JordanListView.as_view()),
    path('<int:jordan_pk>/', JordanDetailView.as_view()),
]