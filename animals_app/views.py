from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Animal, AnimalClassification, AnimalLocalName
from .serializers import AnimalSerializer, AnimalClassificationSerializer, AnimalLocalNameSerializer

class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = AnimalSerializer

class AnimalClassificationListCreateView(generics.ListCreateAPIView):
    queryset = AnimalClassification.objects.all()
    serializer_class = AnimalClassificationSerializer

class AnimalClassificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalClassification.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = AnimalClassificationSerializer

class AnimalLocalNameListCreateView(generics.ListCreateAPIView):
    queryset = AnimalLocalName.objects.all()
    serializer_class = AnimalLocalNameSerializer

class AnimalLocalNameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalLocalName.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = AnimalLocalNameSerializer
