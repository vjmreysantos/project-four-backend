from jwt_auth.admin import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Comment, Jordan

User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PopulatedCommentSerializer(CommentSerializer):
    owner = NestedUserSerializer()

class JordanSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    liked_by = NestedUserSerializer(many=True, read_only=True)

    class Meta:
        model = Jordan
        fields = '__all__'