from django.urls import path
from .views import (
    JordanListView,
    JordanDetailView,
    CommentListView,
    CommentDetailView,
    JordanLikeView,
)

urlpatterns = [
    path('', JordanListView.as_view()),
    path('<int:pk>/', JordanDetailView.as_view()),
    path('<int:jordan_pk>/comments/', CommentListView.as_view()),
    path('<int:jordan_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view()),
    path('<int:jordan_pk>/like/', JordanLikeView.as_view())
]
