import statistics
from requests import Response
from rest_framework import generics
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from animals_app.models import *
from .serializers import *
from rest_framework.views import APIView
#from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth import login
# from django.contrib.auth import logout
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.decorators import login_required



class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['local_name', 'english_name', 'scientific_name']



class AnimalClassificationListCreateView(generics.ListCreateAPIView):
    queryset = AnimalClassification.objects.all()
    serializer_class = AnimalClassificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class AnimalClassificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalClassification.objects.all()
    serializer_class = AnimalClassificationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['local_name', 'english_name', 'scientific_name']


class AnimalEntriesAPIView(APIView):
    def get(self, request):
        total_entries = Animal.compute_animal_entries()
        return Response({'total_entries': total_entries}, status=statistics.HTTP_200_OK)
