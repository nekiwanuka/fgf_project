from django.urls import path
from .views import (
    AnimalListCreateView, AnimalDetailView,
    AnimalClassificationListCreateView, AnimalClassificationDetailView,
    AnimalLocalNameListCreateView, AnimalLocalNameDetailView
)

urlpatterns = [
    path('animals/', AnimalListCreateView.as_view(), name='animal-list-create'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),
    path('classifications/', AnimalClassificationListCreateView.as_view(), name='classification-list-create'),
    path('classifications/<int:pk>/', AnimalClassificationDetailView.as_view(), name='classification-detail'),
    path('localnames/', AnimalLocalNameListCreateView.as_view(), name='localname-list-create'),
    path('localnames/<int:pk>/', AnimalLocalNameDetailView.as_view(), name='localname-detail'),
]
