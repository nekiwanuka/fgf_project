# app_name/serializers.py
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'is_staff', 'is_active')


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'password', 'username')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class UserLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(UserLoginSerializer, cls).get_token(user)
        # You can include additional user data in the token here if needed
        #print("User is here " + user)
        return token
    
    class Meta:
        model = User
        fields = ('username', 'password', 'token')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


""" 
class AdministratorSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Administrator
        exclude = ['registered_by','lastupdated_by']
        depth = 2

class AdministratorLoginSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=254, min_length=5)
    password = serializers.CharField(
        max_length=254,
        min_length=6,
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        login_data = attrs
        return UserFacade().login(login_data)
    

class UpdateUserProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = [
            'password', 
            'is_superuser', 
            'username', 
            'is_staff',
            'is_active', 
            'groups', 
            'user_permissions',
            'is_verified',
            'is_admin',
            'is_fgf_staff',
            'is_contributor',
            'last_login',
            'date_joined'
            ]
        extra_kwargs = {
            'id':{
                'read_only':True
            }
        }

        depth = 3 """