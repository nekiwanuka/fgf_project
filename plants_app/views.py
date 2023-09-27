import statistics
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from plants_app.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
#from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth import login
# from django.contrib.auth import logout
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.decorators import login_required




# Medicinal_Use views

class MedicinalUseListView(generics.ListCreateAPIView):
    queryset = MedicinalUse.objects.all()
    serializer_class = MedicinalUseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['health_issue', 'dosage_and_formulation', 'part_used']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
  
    

class MedicinalUseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicinalUse.objects.all()
    serializer_class = MedicinalUseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Plant views

class PlantListView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = ['local_name', 'english_name', 'scientific_name']



class PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Medicinal Plant views

class MedicinalPlantListView(generics.ListCreateAPIView):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   
    search_fields = ['medicinal_use', 'plant', 'local_name']



class MedicinalPlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
# Plant Entries APIview for calculating the number of plant entries
class PlantEntriesAPIView(APIView):
    def get(self, request):
        total_entries = Plant.compute_plant_entries()
        return Response({'total_entries': total_entries}, status=statistics.HTTP_200_OK)