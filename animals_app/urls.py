from django.urls import path
from .views import *

urlpatterns = [
    path('animals/', AnimalListCreateView.as_view(), name='animal-list-create'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),

    path('animal-classifications/', AnimalClassificationListCreateView.as_view(), name='animal-classification-list-create'),
    path('animal-classifications/<int:pk>/', AnimalClassificationDetailView.as_view(), name='animal-classification-detail'),

    #URLS for AnimalEntries Calculation view
     path('animal_entries/', AnimalEntriesAPIView.as_view(), name='animal-entries'),


]




