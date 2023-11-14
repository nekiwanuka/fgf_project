from rest_framework import serializers
from .models import Plant, MedicinalPlant, PlantName

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class MedicinalPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinalPlant
        fields = '__all__'

class PlantNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantName
        fields = '__all__'