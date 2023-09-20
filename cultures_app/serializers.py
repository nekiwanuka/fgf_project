from rest_framework import serializers
from cultures_app.models import *


class ClanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clan
        fields = "__all__"


class Cultural_KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultural_Kingdom
        fields = "__all__"


class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnicity
        fields = "__all__"


class Cultural_IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultural_Identity
        fields = "__all__"


class Ethnic_GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnic_Group
        fields = "__all__"
