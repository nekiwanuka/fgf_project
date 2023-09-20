from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from cultures_app.models import (
    Clan,
    Cultural_Kingdom,
    Ethnicity,
    Cultural_Identity,
    Ethnic_Group,
)
from .serializers import (
    ClanSerializer,
    Cultural_KingdomSerializer,
    EthnicitySerializer,
    Cultural_IdentitySerializer,
    Ethnic_GroupSerializer,
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


class Cultural_KingdomListview(generics.ListCreateAPIView):
    queryset = Cultural_Kingdom.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = Cultural_KingdomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnicity_name"]


class Cultural_KingdomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cultural_Kingdom.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = Cultural_KingdomSerializer
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


class Cultural_IdentityListview(generics.ListCreateAPIView):
    queryset = Cultural_Identity.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = Cultural_IdentitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnic_group"]


class Cultural_IdentityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cultural_Identity.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = Cultural_IdentitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class Ethnic_GroupListview(generics.ListCreateAPIView):
    queryset = Ethnic_Group.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = Ethnic_GroupSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["ethnic_group"]


class Ethnic_GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ethnic_Group.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = Ethnic_GroupSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
