from rest_framework import serializers
from .models import MedicinalUse, Plant, MedicinalPlant

class MedicinalUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinalUse
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class MedicinalPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinalPlant
        fields = '__all__'
    