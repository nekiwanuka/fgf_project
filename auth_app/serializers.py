from rest_framework import serializers
from auth_app.models import User_Manager



class UserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Manager
        fields = ('__all__') #('email','password')