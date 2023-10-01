import django_filters
from .models import Plant, MedicinalPlant, PlantName

class PlantFilter(django_filters.FilterSet):
    class Meta:
        model = Plant
        fields = {
            'english_name': ['exact', 'icontains'],
            'scientific_name': ['exact', 'icontains'],
            # Add more fields to filter as needed
        }

class MedicinalPlantFilter(django_filters.FilterSet):
    class Meta:
        model = MedicinalPlant
        fields = {
            'health_issues': ['icontains'],
            'part_used_for_health_issues': ['icontains'],
            # Add more fields to filter as needed
        }
class PlantNameFilter(django_filters.FilterSet):
    class Meta:
        model = PlantName
        fields = {
            'local_name': ['exact', 'icontains'],
            'language': ['exact', 'icontains'],
            # Add more fields to filter as needed
        }