from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django_filters import filters
from rest_framework.permissions import IsAuthenticated
from .models import (
    Region,
    LifeForm,
    Value,
    ValueDetail,
    OtherValueDetail,
    Plant,
    PlantLocalName,
    MedicinalPlant
)
from .serializers import (
    RegionSerializer,
    LifeFormSerializer,
    ValueSerializer,
    ValueDetailSerializer,
    OtherValueDetailSerializer,
    PlantSerializer,
    PlantLocalNameSerializer,
    MedicinalPlantSerializer
)

class RegionListView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

class RegionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

class LifeFormListView(generics.ListCreateAPIView):
    queryset = LifeForm.objects.all()
    serializer_class = LifeFormSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

class LifeFormDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LifeForm.objects.all()
    serializer_class = LifeFormSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

class ValueListView(generics.ListCreateAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

class ValueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

class ValueDetailListView(generics.ListCreateAPIView):
    queryset = ValueDetail.objects.all()
    serializer_class = ValueDetailSerializer
    permission_classes = [IsAuthenticated]

class ValueDetailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ValueDetail.objects.all()
    serializer_class = ValueDetailSerializer
    permission_classes = [IsAuthenticated]

class OtherValueDetailListView(generics.ListCreateAPIView):
    queryset = OtherValueDetail.objects.all()
    serializer_class = OtherValueDetailSerializer
    permission_classes = [IsAuthenticated]

class OtherValueDetailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OtherValueDetail.objects.all()
    serializer_class = OtherValueDetailSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

class PlantListView(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

class PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

class PlantLocalNameListView(generics.ListCreateAPIView):
    queryset = PlantLocalName.objects.all()
    serializer_class = PlantLocalNameSerializer
    permission_classes = [IsAuthenticated]

class PlantLocalNameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlantLocalName.objects.all()
    serializer_class = PlantLocalNameSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

class MedicinalPlantListView(generics.ListCreateAPIView):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    permission_classes = [IsAuthenticated]

class MedicinalPlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    permission_classes = [IsAuthenticated]
