from rest_framework import serializers
from .models import Plant, MedicinalPlant, PlantName

class PlantNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantName
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    plant_names = PlantNameSerializer(many=True)  # Serialize plant names

    class Meta:
        model = Plant
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Serialize plant names for each plant
        plant_names_data = PlantNameSerializer(instance.plant_names.all(), many=True).data
        representation['plant_names'] = plant_names_data
        return representation
    
    
class MedicinalPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinalPlant
        fields = '__all__'