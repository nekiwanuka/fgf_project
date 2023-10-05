from rest_framework import serializers
from .models import *


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class LifeFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeForm
        fields = '__all__'

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'

class ValueDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueDetail
        fields = '__all__'

class OtherValueDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherValueDetail
        fields = '__all__'

class PlantLocalNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantLocalName
        fields = '__all__'

class MedicinalPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinalPlant
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    # Serialize the ManyToMany fields
    region = RegionSerializer(many=True)
    life_form = LifeFormSerializer(many=True)
    values = ValueDetailSerializer(many=True)
    other_value_details = OtherValueDetailSerializer(many=True)
    plant_local_names = PlantLocalNameSerializer(many=True)
    medicinal_plant = MedicinalPlantSerializer()

    class Meta:
        model = Plant
        fields = '__all__'
