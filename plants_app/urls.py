from django.urls import path
from .views import Medicinal_UseListView, Medicinal_UseDetailView, PlantListView, PlantDetailView

urlpatterns = [
    # URLs for Medicinal_Use model
    path('medicinal_uses/', Medicinal_UseListView.as_view(), name='medicinal-use-list'),
    path('medicinal_uses/<int:pk>/', Medicinal_UseDetailView.as_view(), name='medicinal-use-detail'),

    # URLs for Plant model
    path('plants/', PlantListView.as_view(), name='plant-list'),
    path('plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
]
