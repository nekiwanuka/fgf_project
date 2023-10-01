from rest_framework import serializers
from .models import Plant, PlantName, MedicinalPlant

class PlantNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantName
        fields = ['local_name', 'language']

class PlantSerializer(serializers.ModelSerializer):
    plant_names = PlantNameSerializer(many=True, read_only=True)

    class Meta:
        model = Plant
        fields = '__all__'

class MedicinalPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinalPlant
        fields = '__all__'
