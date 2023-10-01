from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Plant, PlantName, MedicinalPlant
from .serializers import PlantSerializer, PlantNameSerializer, MedicinalPlantSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    @action(detail=True, methods=['post'])
    def add_local_name(self, request, pk=None):
        plant = self.get_object()

        local_name = request.data.get('local_name')
        language = request.data.get('language')

        if local_name and language:
            plant_name = PlantName.objects.create(plant=plant, local_name=local_name, language=language)
            serializer = PlantNameSerializer(plant_name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Both local name and language are required."}, status=status.HTTP_400_BAD_REQUEST)

class PlantNameViewSet(viewsets.ModelViewSet):
    queryset = PlantName.objects.all()
    serializer_class = PlantNameSerializer

class MedicinalPlantViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer

    def perform_create(self, serializer):
        # Automatically set medicinal_values_entered to True
        serializer.save(medicinal_values_entered=True)

    # You can add more actions as needed for the MedicinalPlant model

# Add other views as needed for your application
