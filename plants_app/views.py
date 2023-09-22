from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import MedicinalUse, Plant, MedicinalPlant
from .serializers import MedicinalUseSerializer, PlantSerializer, MedicinalPlantSerializer

# Medicinal_Use views

class MedicinalUseListView(generics.ListCreateAPIView):
    queryset = MedicinalUse.objects.all()
    serializer_class = MedicinalUseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['health_issue', 'dosage_and_formulation', 'part_used']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MedicinalUseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicinalUse.objects.all()
    serializer_class = MedicinalUseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Plant views

class PlantListView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['local_name', 'english_name', 'scientific_name']

class PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Medicinal Plant views

class MedicinalPlantListView(generics.ListCreateAPIView):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   
    search_fields = ['medicinal_use', 'plant']

class MedicinalPlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
