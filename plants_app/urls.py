from django.urls import path
from .views import *

urlpatterns = [
    # URLs for Medicinal_Use model
    path('medicinal_uses/', Medicinal_UseListView.as_view(), name='medicinal-use-list'),
    path('medicinal_uses/<int:pk>/', Medicinal_UseDetailView.as_view(), name='medicinal-use-detail'),

    # URLs for Plant model
    path('plants/', PlantListView.as_view(), name='plant-list'),
    path('plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),

    # URLs for Medicinal_Plant model
    path('medicinal_plants/', Medicinal_PlantListView.as_view(), name='medicinal-plant-list'),
    path('medicinal_plants/<int:pk>/', Medicinal_PlantDetailView.as_view(), name='medicinal-plant-detail'),
]
