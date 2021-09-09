from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Jordan
from .serializers import JordanSerializer

class JordanListView(APIView):
    ''' List View for /jordans GET POST'''

    def get(self, _request):
        ''' Index '''
        jordans = Jordan.objects.all()
        serialized = JordanSerializer(jordans, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class JordanDetailView(APIView):
    ''' Detail View for /jordan/id SHOW UPDATE DELETE '''

    def get(self, _request, jordan_pk):
        jordan = Jordan.objects.get(pk=jordan_pk)
        serialized = JordanSerializer(jordan)
        return Response(serialized.data, status=status.HTTP_200_OK)