from rest_framework import serializers
from .models import Medicinal_Use, Plant, Medicinal_Plant

class Medicinal_UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicinal_Use
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class Medicinal_PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicinal_Plant
        fields = '__all__'
    