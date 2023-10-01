from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlantViewSet, PlantNameViewSet, MedicinalPlantViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'plants', PlantViewSet)
router.register(r'plantnames', PlantNameViewSet)
router.register(r'medicinalplants', MedicinalPlantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Add other URL patterns as needed for your application
