from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Jordan
from .serializers import JordanSerializer

class JordanListView(ListCreateAPIView):
    ''' List View for /jordans Index CREATE '''

    queryset = Jordan.objects.all()
    serializer_class = JordanSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class JordanDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /jordan/id SHOW UPDATE DELETE '''

    queryset = Jordan.objects.all()
    serializer_class = JordanSerializer

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
