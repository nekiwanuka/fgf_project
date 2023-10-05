from django.urls import path
from .views import (
    RegionListView,
    RegionDetailView,
    LifeFormListView,
    LifeFormDetailView,
    ValueListView,
    ValueDetailView,
    ValueDetailListView,
    ValueDetailDetailView,
    OtherValueDetailListView,
    OtherValueDetailDetailView,
    PlantListView,
    PlantDetailView,
    PlantLocalNameListView,
    PlantLocalNameDetailView,
    MedicinalPlantListView,
    MedicinalPlantDetailView
)

urlpatterns = [
    path('regions/', RegionListView.as_view(), name='region-list'),
    path('regions/<int:pk>/', RegionDetailView.as_view(), name='region-detail'),
    path('lifeforms/', LifeFormListView.as_view(), name='lifeform-list'),
    path('lifeforms/<int:pk>/', LifeFormDetailView.as_view(), name='lifeform-detail'),
    path('values/', ValueListView.as_view(), name='value-list'),
    path('values/<int:pk>/', ValueDetailView.as_view(), name='value-detail'),
    path('valuedetails/', ValueDetailListView.as_view(), name='valuedetail-list'),
    path('valuedetails/<int:pk>/', ValueDetailDetailView.as_view(), name='valuedetail-detail'),
    path('othervaluedetails/', OtherValueDetailListView.as_view(), name='othervaluedetail-list'),
    path('othervaluedetails/<int:pk>/', OtherValueDetailDetailView.as_view(), name='othervaluedetail-detail'),
    path('plants/', PlantListView.as_view(), name='plant-list'),
    path('plants/<int:pk>/', PlantDetailView.as_view(), name='plant-detail'),
    path('plantlocalnames/', PlantLocalNameListView.as_view(), name='plantlocalname-list'),
    path('plantlocalnames/<int:pk>/', PlantLocalNameDetailView.as_view(), name='plantlocalname-detail'),
    path('medicinalplants/', MedicinalPlantListView.as_view(), name='medicinalplant-list'),
    path('medicinalplants/<int:pk>/', MedicinalPlantDetailView.as_view(), name='medicinalplant-detail'),
]
