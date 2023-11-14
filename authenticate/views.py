from django.shortcuts import render
from rest_framework import generics, status, authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserDetailView(APIView): #ListCreateAPIView
    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    #serializer_class = UserSerializer
    #queryset = UserSerializer.objects.all()

    def get(self, request):
        user = request.user
        data = {
            'username': user.username,
            'email': user.email,
        }
        #serializer_class = UserSerializer(request.user)
        return Response(data)
        #return Response({'username': request.user.username})


# class UserLoginView(TokenObtainPairView):
#     serializer_class = UserSerializer


User = get_user_model()

class CustomUserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = []  # Allow unauthenticated access

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'detail': 'User registered successfully.'}, status=status.HTTP_201_CREATED)


# class CustomUserLoginView(TokenObtainPairView):
#     serializer_class = UserLoginSerializer
#     permission_classes = []
    
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         if serializer.is_valid():
#             data = serializer.validated_data
            
#             return Response(data=data, status=status.HTTP_200_OK)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class CustomUserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
    permission_classes = []
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            data = serializer.validated_data
            return Response(data, status.HTTP_200_OK)


@login_required
# class seeView(generics.ListAPIView):
def see(request):
    # Your view logic here
    return JsonResponse({'message': 'Hello, this is the see view!'})
