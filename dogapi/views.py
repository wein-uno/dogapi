from django.shortcuts import render
from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer

class DogViewSet(viewsets.ModelViewSet):
       queryset = Dog.objects.all()
       serializer_class = DogSerializer

class BreedViewSet(viewsets.ModelViewSet):
       queryset = Breed.objects.all()
       serializer_class = BreedSerializer

