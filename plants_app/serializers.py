from rest_framework import serializers
from .models import Medicinal_Use, Plant

class Medicinal_UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicinal_Use
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'
