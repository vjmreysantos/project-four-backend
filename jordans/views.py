from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Jordan, Comment
from .serializers import JordanSerializer, CommentSerializer

class JordanListView(ListCreateAPIView):
    ''' List View for /jordans Index CREATE '''

    queryset = Jordan.objects.all()
    serializer_class = JordanSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class JordanDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /jordan/id SHOW UPDATE DELETE '''

    queryset = Jordan.objects.all()
    serializer_class = JordanSerializer

class CommentListView(APIView):
    ''' List View for /jordans/jordanId/comments CREATE comments '''

    def post(self, request, jordan_pk):

        request.data['jordan'] = jordan_pk
        created_comment = CommentSerializer(data=request.data)
        if created_comment.is_valid():
            created_comment.save()
            return Response(created_comment.data, status=status.HTTP_201_CREATED)
        return Response(created_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        

class CommentDetailView(APIView):
    ''' DELETE Comment View '''

    def delete(self, _request, **kwargs):

        comment_pk = kwargs['comment_pk']
        try:
            comment_to_delete = Comment.objects.get(pk=comment_pk)
            comment_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound(detail='Comment not found')

class JordanLikeView(APIView):
    ''' Adds likes to characters or removes if already liked '''

    def post(self, request, jordan_pk):

        try:
            jordan_to_like = Jordan.objects.get(pk=jordan_pk)
        except Jordan.DoesNotExist:
            raise NotFound()

        if request.user in jordan_to_like.liked_by.all():
            jordan_to_like.liked_by.remove(request.user.id)
        else:
            jordan_to_like.liked_by.add(request.user.id)

        serialized_jordan = JordanSerializer(jordan_to_like)

        return Response(serialized_jordan.data, status=status.HTTP_202_ACCEPTED)


