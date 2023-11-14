from django.urls import path
from .views import *
from rest_auth.views import (
    LogoutView, PasswordChangeView,
)

urlpatterns = [
    # path('register/', UserCreateView.as_view(), name='user-create'),
    # path('login/', UserLoginView.as_view(), name='user-login'),
    path('api/register/', CustomUserRegistrationView.as_view(),
         name='user-registration'),
    path('api/login/', CustomUserLoginView.as_view(), name='user-login'),
    
    path('api/profile/', UserDetailView.as_view(), name='profile'),
    path('see/', see, name='see'),

    path(r'api/logout/', LogoutView.as_view(), name='rest_logout'),
]
