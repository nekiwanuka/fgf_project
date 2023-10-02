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
    # Add fields for plant names and local names with languages
    plant_english_name = serializers.CharField(source='plant.english_name', read_only=True)
    plant_scientific_name = serializers.CharField(source='plant.scientific_name', read_only=True)
    #plant_local_names = PlantLocalNameSerializer(source='plant.plant_local_name', many=True, read_only=True)

    # Modify the to_representation method to include language for each local name
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        plant_local_names = representation.get('plant_local_names', [])

        modified_local_names = []
        for local_name in plant_local_names:
            local_name_with_language = f"{local_name['local_name']} ({local_name['language']})"
            modified_local_names.append(local_name_with_language)

        representation['plant_local_names'] = modified_local_names
        return representation

    class Meta:
        model = MedicinalPlant
        fields = '__all__'