from rest_framework import serializers
#from allauth.account.models import EmailAddress
from auth_app.models import User

#Commented out for now
#from api._serializers.useremailaddress_serializers import UserEmailAddressSerializer
#from api._serializers.userwebsite_serializers import UserWebsiteSerializer
#from api._serializers.userphonenumber_serializers import UserPhoneNumberSerializer
#from api._serializers.usersocialaccount_serializers import UserSocialAccountSerializer
#from api._serializers.userphoto_serializers import UserPhotoSerializer
#from api._serializers.useraddress_serializers import UserAddressSerializer

from core.mixins.serializer_mixins import ModelSerializer

class RegisterUserSerializer(ModelSerializer):
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
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)

        EmailAddress.objects.create(
            user=user, email=user.email, verified=True, primary=True)
        return user


class UserSerializer(ModelSerializer):
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
            ]
        extra_kwargs={}


""" class UserProfileSerializer(ModelSerializer):
    emails = UserEmailAddressSerializer(read_only=True, many=True)
    phone_numbers = UserPhoneNumberSerializer(read_only=True, many=True)
    photos = UserPhotoSerializer(read_only=True, many=True)
    social_accounts = UserSocialAccountSerializer(read_only=True, many=True)
    websites = UserWebsiteSerializer(read_only=True, many=True)
    addresses = UserAddressSerializer(read_only=True, many=True)

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
            ]

        depth = 3 """
    

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

        depth = 3