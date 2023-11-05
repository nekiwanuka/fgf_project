from . import views

#for login, logout and registration
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView
from rest_framework_simplejwt import views as jwt_views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
"""
    This module is an aggregate of all the auth urls / endpoints.
"""

from django.urls import path, re_path
from ._urls import administrator_urls as administrator_urls
from ._urls import contributor_urls as contributor_urls

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_auth.views import (
    LogoutView, PasswordChangeView,
)


from auth_app.views import (
    # RegisterUserView, 
    VerifyEmailView,
    SendVerificationLinkView, 
    # UserLoginView,
    PasswordResetView, PasswordResetConfirmView
)

# aggregate auth urls
administrator_urls
contributor_urls


urlpatterns = [
    # jwt : Get Access token and its coresponding Refresh Token
    path(r'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # jwt : User a Refresh Token to refresh the Access Token
    path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registration and social media authentication
    # path(r'registration/register/', RegisterUserView.as_view(),
    #      name='account_signup_or_register'),
    # path(r'auth/registration/', include('rest_auth.registration.urls')),

    # Verifies email for successfull Registration
    path(
        'verify-email',
        VerifyEmailView.as_view(),
        name='verify-email'
    ),

    # Resends email verification link for successfull Registration
    path(
        'verification-link/',
        SendVerificationLinkView.as_view(),
        name='email-verification-link'
    ),

    # URLs that do not require a session or valid token
    path(r'password/reset/', PasswordResetView.as_view(),
         name='rest_password_reset'),
    path(r'password/reset/confirm/', PasswordResetConfirmView.as_view(),
         name='rest_password_reset_confirm'),

   
    # path(
    #     r'login/',
    #     UserLoginView.as_view(),
    #     name='login'
    # ),

    # URLs that require a user to be logged in with a valid session / token.
    path(r'logout/', LogoutView.as_view(), name='rest_logout'),
    path(r'password/change/', PasswordChangeView.as_view(),
         name='rest_password_change'),
]

# urlpatterns = [
#     #path('users/', UserListCreateView.as_view(), name='user-list'),
#     #path('users/<uuid:pk>/', UserDetailView.as_view(), name='user-detail'),
#     #path('administrators/', AdministratorListCreateView.as_view(), name='administrator-list'),
#     #path('administrators/<uuid:pk>/', AdministratorDetailView.as_view(), name='administrator-detail'),
#     #path('contributors/', ContributorListCreateView.as_view(), name='contributor-list'),
#     #path('contributors/<uuid:pk>/', ContributorDetailView.as_view(), name='contributor-detail'),
    
#     #path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     path('register/', RegisterView.as_view()),
#     #path('login/', LoginView.as_view()),
#     re_path('login', views.login),
#     #re_path('signup', views.signup),
#     re_path('test_token', views.test_token),

#     path('logout/', LogoutView.as_view()),

#     path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
#     path('confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
#     re_path(r'^confirm-email/(?P<key>[-:\w]+)/$',
#              VerifyEmailView.as_view(), name='account_confirm_email'),

# ]