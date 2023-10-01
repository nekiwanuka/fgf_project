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
    english_name = serializers.CharField(source='plant.english_name', read_only=True)
    scientific_name = serializers.CharField(source='plant.scientific_name', read_only=True)
    local_names = serializers.StringRelatedField(source='plant.plant_names', many=True, read_only=True)

    class Meta:
        model = MedicinalPlant
        fields = ( 'plant', 'english_name', 'scientific_name', 'local_names', 'health_issues', 'part_used_for_health_issues',
                  'preparation_steps', 'dosage', 'contraindications', 'shelf_life', 'notes')
