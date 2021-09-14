from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

from .serializers import (
    UserRegisterSerializer,
    UserProfileSerializer
)

User = get_user_model()

class RegisterView(APIView):

    def post(self, request):
        user_to_create = UserRegisterSerializer(data=request.data)
        if user_to_create.is_valid():
            user_to_create.save()
            return Response(
                {'message': 'Registration successful'},
                status=status.HTTP_201_CREATED
            )
        return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user_to_login = User.objects.get(username=username)
        except User.DoesNotExist:
            raise PermissionDenied(detail='Unauthorized')

        if not user_to_login.check_password(password):
            raise PermissionDenied()

        expiry_time = datetime.now() + timedelta(days=7)
        token = jwt.encode(
            { 'sub': user_to_login.id, 'exp': int(expiry_time.strftime('%s'))},
            settings.SECRET_KEY,
            algorithm='HS256'
        )

        return Response({
            'token': token,
            'message': f'Welcome back {username}'
        }, status=status.HTTP_200_OK)

class ProfileListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serialized_users = UserRegisterSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)

class ProfileView(APIView):

    permission_classes = (IsAuthenticated, )

    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound()
    
    def get(self, request):
        user = self.get_user(username=request.user.username)
        serialized_user = UserProfileSerializer(user)
        return Response(serialized_user.data)

    def put(self, request):
        user_to_update = self.get_user(username= request.user.username)
        updated_user = UserProfileSerializer(user_to_update, data=request.data, context={'request': 'update'})
        if updated_user.is_valid():
            updated_user.save()
            return Response(updated_user.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_user.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request):
        user_to_delete = self.get_user(username= request.user.username)
        user_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileDetailView(APIView):

    permission_classes = (IsAuthenticated, )

    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound()

    def get(self, _request, username):
        user = self.get_user(username)
        serialized_user = UserRegisterSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)