from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from cultures_app.models import (
    Clan,
    CulturalKingdom,
    Ethnicity,
    CulturalIdentity,
    EthnicGroup,
)
from .serializers import (
    ClanSerializer,
    CulturalKingdomSerializer,
    EthnicitySerializer,
    CulturalIdentitySerializer,
    EthnicGroupSerializer,
)


# Create your views here.
class ClanListview(generics.ListCreateAPIView):
    queryset = Clan.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ClanSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["clan_name"]


class ClanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clan.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ClanSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class CulturalKingdomListview(generics.ListCreateAPIView):
    queryset = CulturalKingdom.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CulturalKingdomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnicity_name"]


class CulturalKingdomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CulturalKingdom.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CulturalKingdomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class EthnicityListview(generics.ListCreateAPIView):
    queryset = Ethnicity.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EthnicitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnicity_name"]


class EthnicityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ethnicity.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EthnicitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class CulturalIdentityListview(generics.ListCreateAPIView):
    queryset = CulturalIdentity.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CulturalIdentitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnic_group"]


class CulturalIdentityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CulturalIdentity.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CulturalIdentitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class EthnicGroupListview(generics.ListCreateAPIView):
    queryset = EthnicGroup.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EthnicGroupSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnic_group"]


class EthnicGroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EthnicGroup.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EthnicGroupSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
