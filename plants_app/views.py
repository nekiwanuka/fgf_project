from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Plant, PlantLocalName, MedicinalPlant
from .serializers import PlantSerializer, PlantLocalNameSerializer, MedicinalPlantSerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['english_name', 'scientific_name']

    @action(detail=True, methods=['post'])
    def add_plant_name(self, request, pk=None):
        plant = self.get_object()

        local_name = request.data.get('local_name')
        language = request.data.get('language')

        if local_name and language:
            plant_name = PlantLocalName.objects.create(plant=plant, local_name=local_name, language=language)
            serializer = PlantLocalNameSerializer(plant_name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Both local name and language are required."}, status=status.HTTP_400_BAD_REQUEST)


class PlantLocalNameViewSet(viewsets.ModelViewSet):
    queryset = PlantLocalName.objects.all()
    serializer_class = PlantLocalNameSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['local_name', 'language']


class MedicinalPlantViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['plant__english_name', 'plant__scientific_name']
