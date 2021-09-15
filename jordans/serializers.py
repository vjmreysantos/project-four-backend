from jwt_auth.admin import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Jordan

User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image')

class JordanSerializer(serializers.ModelSerializer):
    liked_by = NestedUserSerializer(many=True, read_only=True)

    class Meta:
        model = Jordan
        fields = '__all__'