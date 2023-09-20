from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from animals_app.models import Animal, Animal_Classification
from .serializers import AnimalSerializer, Animal_ClassificationSerializer

# Animal views

class AnimalListView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AnimalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['local_name']


class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AnimalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    


# Animal_Classification views

class Animal_ClassificationListView(generics.ListCreateAPIView):
    queryset = Animal_Classification.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = Animal_ClassificationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class Animal_ClassificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal_Classification.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = Animal_ClassificationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
