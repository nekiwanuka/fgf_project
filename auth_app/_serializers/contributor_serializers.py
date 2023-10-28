from rest_framework import serializers

from auth_app.models import User, Contributor
from business_logic.system_users._user import User as UserFacade
from core.mixins.serializer_mixins import ModelSerializer
from .user_serializers import UserSerializer
from business_logic.system_users import Contributor as UserFacade
from django.views.decorators.http import require_http_methods
#from auth_app.facade import UserFacade  # Import your UserFacade or User registration logic


# class CreateContributorSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         max_length=254, 
#         min_length=5,
#         required=True,
#         write_only=True,
#         )
#     password = serializers.CharField(
#         max_length=254,
#         min_length=6,
#         required=True,
#         write_only=True,
#         help_text='Required',
#         style={'input_type': 'password', 'placeholder': 'Password'}
#     )
#     data = serializers.DictField(
#         required=False,
#         read_only=True,
#         )

#     class Meta:
#         model = User
#         fields = ['email', 'password','data']
#         #fields = ['email', 'password']

#     """ def create(self, validated_data):
#         # Create and return a new user instance using the validated data
#         user = User.objects.create(
#             email=validated_data['email']
#         )
#         user.set_password(validated_data['password'])  # Hash and set the password
#         user.save()
#         return user """

#     @require_http_methods(["GET", "POST"])
#     def create(self, validated_data):
#         _request = self.context['request']
#         request = {'request':_request, 'validated_data':validated_data}
#         return UserFacade().register_contributor(request)


class CreateContributorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=254, 
        min_length=5,
        required=True,
        write_only=True,
    )
    password = serializers.CharField(
        max_length=254,
        min_length=6,
        required=True,
        write_only=True,
        help_text='Required',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    @require_http_methods(["GET", "POST"])
    def create(self, validated_data):
        # Create and return a new user instance using the validated data
        user = User.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Hash and set the password
        #user.save()
       
        _request = self.context['request']
        request = {'request':_request, 'validated_data':validated_data}
        #return user
        return UserFacade().register_contributor(request)


class ContributorSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Contributor
        exclude = ['registered_by','lastupdated_by']
        depth = 2


class ContributorLoginSerializer(ModelSerializer):
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
