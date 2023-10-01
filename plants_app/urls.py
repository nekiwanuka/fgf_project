from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlantViewSet, PlantLocalNameViewSet, MedicinalPlantViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'plants', PlantViewSet)
router.register(r'plant-names', PlantLocalNameViewSet)
router.register(r'medicinal-plants', MedicinalPlantViewSet)



# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
