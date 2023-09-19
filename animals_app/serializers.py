from rest_framework import serializers
from animals_app.models import *


class Animal_ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal_Classification
        fields = ('__all__')
        
        
        
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('__all__')
        
# Context from Class or Interface animals_app/models.py:Animal_Classification
# Class Animal_Classification:
# 	Fields:
# 		kingdom_name = models.CharField(max_length=250)
# 		species = models.CharField(max_length=250)
# 		number_of_species = models.IntegerField(default=1, null=True)
# 		animal_class = models.CharField(max_length=250)
# 		order = models.CharField(max_length=250)
# 	Methods:
#