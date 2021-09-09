from django.db.models import fields
from rest_framework import serializers
from .models import Jordan

class JordanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jordan
        fields = '__all__'