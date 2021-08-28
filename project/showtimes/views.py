from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from showtimes.models import Cinema
from showtimes.serializers import CinemaSerializer


class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
