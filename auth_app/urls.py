from . import views

from django.urls import path, re_path
from .views import UserListCreateView, UserDetailView, \
    AdministratorListCreateView, AdministratorDetailView, \
    ContributorListCreateView, ContributorDetailView

from rest_framework_simplejwt.views import TokenRefreshView
from .views import TokenObtainPairView  # Import your custom token view

#for login, logout and registration
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('administrators/', AdministratorListCreateView.as_view(), name='administrator-list'),
    path('administrators/<uuid:pk>/', AdministratorDetailView.as_view(), name='administrator-detail'),
    path('contributors/', ContributorListCreateView.as_view(), name='contributor-list'),
    path('contributors/<uuid:pk>/', ContributorDetailView.as_view(), name='contributor-detail'),
    
    #path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterView.as_view()),
    #path('login/', LoginView.as_view()),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),

    path('logout/', LogoutView.as_view()),

    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^confirm-email/(?P<key>[-:\w]+)/$',
             VerifyEmailView.as_view(), name='account_confirm_email'),

]
