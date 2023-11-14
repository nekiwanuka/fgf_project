from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserRegistrationSerializer, CustomUserLoginSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# class UserCreateView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserLoginView(TokenObtainPairView):
#     serializer_class = UserSerializer


User = get_user_model()


class CustomUserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserRegistrationSerializer
    permission_classes = []  # Allow unauthenticated access

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'detail': 'User registered successfully.'}, status=status.HTTP_201_CREATED)


class CustomUserLoginView(TokenObtainPairView):
    serializer_class = CustomUserLoginSerializer


@login_required
# class seeView(generics.ListAPIView):
def see(request):
    # Your view logic here
    return JsonResponse({'message': 'Hello, this is the see view!'})
