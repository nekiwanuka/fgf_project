from rest_framework import serializers
from .models import Plant, PlantLocalName, MedicinalPlant

class PlantLocalNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantLocalName
        fields = ['local_name', 'language']

class PlantSerializer(serializers.ModelSerializer):
    plant_names = PlantLocalNameSerializer(many=True, read_only=True)

    class Meta:
        model = Plant
        fields = '__all__'

class MedicinalPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinalPlant
        fields = '__all__'
