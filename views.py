import django_filters
from django.shortcuts import render
from . models import Car
from rest_framework import generics
from .serializers import CarSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from . permissions import AllForAdminOtherReadOnly
from rest_framework import filters

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllForAdminOtherReadOnly, )
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.OrderingFilter]
    search_fields = ['brand', 'mark', 'year']


