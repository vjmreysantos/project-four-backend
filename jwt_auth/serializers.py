
from jordans.serializers import JordanSerializer, CommentSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'Does not match'})

        data['password'] = make_password(password)

        return data

    class Meta:
        model = User
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    liked_jordan = JordanSerializer(many=True)
    comments_made = CommentSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'profile_image', 'liked_characters', 'comments_made')