from rest_framework import serializers
from .models import Animal, AnimalClassification

class AnimalClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalClassification
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    animal_classifications = AnimalClassificationSerializer()

    class Meta:
        model = Animal
        fields = '__all__'
