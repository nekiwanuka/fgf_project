from django.urls import path
from .views import (
    CountEntriesAPIView,
    AnimalListCreateView,
    AnimalDetailView,
    AnimalClassificationListCreateView,
    AnimalClassificationDetailView,
    AnimalLocalNameListCreateView,
    AnimalLocalNameDetailView
)

urlpatterns = [
    path('count-entries/', CountEntriesAPIView.as_view(), name='count-entries'),

    path('animals/', AnimalListCreateView.as_view(), name='animal-list-create'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),

    path('animal-classifications/', AnimalClassificationListCreateView.as_view(), name='animal-classification-list-create'),
    path('animal-classifications/<int:pk>/', AnimalClassificationDetailView.as_view(), name='animal-classification-detail'),

    path('animal-local-names/', AnimalLocalNameListCreateView.as_view(), name='animal-local-name-list-create'),
    path('animal-local-names/<int:pk>/', AnimalLocalNameDetailView.as_view(), name='animal-local-name-detail'),
]
