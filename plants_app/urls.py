from django.urls import path
from .views import (
    MedicinalPlantListView,
    MedicinalPlantDetailView,
    PlantListView,
    PlantDetailView,
    PlantNameListView,
    PlantNameDetailView,
    CalculateMedicinalPlantsCount,
    CalculatePlantsCount
)

urlpatterns = [
    path('api/medicinal-plants/', MedicinalPlantListView.as_view(), name='medicinal-plant-list'),
    path('api/medicinal-plants/<int:pk>/', MedicinalPlantDetailView.as_view(), name='medicinal-plant-detail'),
    path('api/plants/', PlantListView.as_view(), name='plant-list'),
    path('api/plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
    path('api/plant-names/', PlantListView.as_view(), name='plant-name-list'),
    path('api/plant-names/<int:pk>/', PlantNameDetailView.as_view(), name='plant-name-detail'),

    path('api/calculate-medicinal-plants-count/', CalculateMedicinalPlantsCount.as_view(), name='calculate-medicinal-plants-count'),
    path('api/calculate-plants-count/', CalculatePlantsCount.as_view(), name='calculate-plants-count'),
    # ... other URL patterns ...
    path('api/plant_images/', PlantListView.as_view(), name='plant-list'), #create view for images
]
