from .models import agahi
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class PosterSerializer(ModelSerializer):
    class Meta:
        model = agahi
        fields = "__all__"


class PosterListSerializer(ModelSerializer):
    class Meta:
        model = agahi
        fields = ['id',"name"]



