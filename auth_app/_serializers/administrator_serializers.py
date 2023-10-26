from rest_framework import serializers

from auth_app.models import User, Administrator
from business_logic.system_users._user import User as UserFacade
from core.mixins.serializer_mixins import ModelSerializer
from .user_serializers import UserSerializer
from business_logic.system_users import Administrator as UserFacade


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


# class CreateAdministratorSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
#     email = serializers.EmailField(max_length=254, min_length=5)
#     password = serializers.CharField(
#         max_length=254,
#         min_length=6,
#         required=True,
#         write_only=True,
#         help_text='Leave empty if no change needed',
#         style={'input_type': 'password', 'placeholder': 'Password'}
#     )

#     class Meta:
#         model = User
#         fields = ['email', 'password']

#     # def validate(self, attrs):
#     #     return attrs

#     def create(self, validated_data):
#         email = validated_data.pop('email', None)
#         user = User.objects.get(email) or User.objects.create_user(**validated_data)
#         admin = Administrator.objects.create(user=user) or None
#         try:
#             if (admin):
#                 user.is_admin = True
#                 user.save(commit=True)
#             return user
#         except Exception as exception:
#             raise exception
