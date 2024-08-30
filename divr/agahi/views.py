from django.shortcuts import render
import request
import json
import rest_framework
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import agahi
from serializers import PosterSerializer, PosterListSerializer

class Agahi(ListCreateAPIView):
    queryset = agahi.object.all()
    serializer_class = PosterSerializer

class Agahilist(ListAPIView):
    queryset = agahi.object.all()
    serializer_class = PosterListSerializer

class Agahidetail(RetrieveUpdateDestroyAPIView):
    queryset = agahi.object.all()
    serializer_class = PosterSerializer

