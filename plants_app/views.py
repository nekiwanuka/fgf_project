from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Medicinal_Use, Plant, Medicinal_Plant
from .serializers import Medicinal_UseSerializer, PlantSerializer, Medicinal_PlantSerializer

# Medicinal_Use views

class Medicinal_UseListView(generics.ListCreateAPIView):
    queryset = Medicinal_Use.objects.all()
    serializer_class = Medicinal_UseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['health_issue', 'dosage_and_formulation', 'part_used']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Medicinal_UseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicinal_Use.objects.all()
    serializer_class = Medicinal_UseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Plant views

class PlantListView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['local_name', 'english_name', 'scientific_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Medicinal Plant views
class Medicinal_PlantListView(generics.ListCreateAPIView):
    queryset = Medicinal_Plant.objects.all()
    serializer_class = Medicinal_PlantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['medicinal_use', 'plant']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   

class Medicinal_PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicinal_Plant.objects.all()
    serializer_class = Medicinal_PlantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
