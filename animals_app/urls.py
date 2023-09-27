from django.urls import path
from .views import AnimalListCreateView, AnimalDetailView, AnimalClassificationListCreateView, AnimalClassificationDetailView

urlpatterns = [
    path('animals/', AnimalListCreateView.as_view(), name='animal-list-create'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),

    path('animal-classifications/', AnimalClassificationListCreateView.as_view(), name='animal-classification-list-create'),
    path('animal-classifications/<int:pk>/', AnimalClassificationDetailView.as_view(), name='animal-classification-detail'),
]
