from django.urls import path
from .views import *

urlpatterns = [
    # URLs for Medicinal_Use model
    path('medicinal_uses/', MedicinalUseListView.as_view(), name='medicinal-use-list'),
    path('medicinal_uses/<int:pk>/', MedicinalUseDetailView.as_view(), name='medicinal-use-detail'),

    # URLs for Plant model
    path('plants/', PlantListView.as_view(), name='plant-list'),
    path('plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),

    # URLs for Medicinal_Plant model
    path('medicinal_plants/', MedicinalPlantListView.as_view(), name='medicinal-plant-list'),
    path('medicinal_plants/<int:pk>/', MedicinalPlantDetailView.as_view(), name='medicinal-plant-detail'),
]
