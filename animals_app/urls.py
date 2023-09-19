from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.AnimalListView.as_view()),
    path('animals/<int:pk>/', views.AnimalDetailView.as_view()),
    path('classification/', views.Animal_ClassificationListView.as_view()),
    path('classification/<int:pk>/', views.Animal_ClassificationDetailView.as_view()),
    
   
    

]