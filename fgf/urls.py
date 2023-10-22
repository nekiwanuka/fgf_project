"""
URL configuration for fgf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from dj_rest_auth.views  import PasswordResetView, PasswordResetConfirmView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/plants/', include('plants_app.urls')),
    path('api/animals/', include('animals_app.urls')),
    path('api/cultures/', include('cultures_app.urls')),

    path('auth_app/', include('rest_authtoken.urls')),
    
    
    path('', include('animals_app.urls'), name='animals'), 
    path('', include('cultures_app.urls'), name='cultures'),
    path('', include('plants_app.urls'), name='plants'), 
    path('', include('auth_app.urls')),

    #urls for password reset
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    
    ]
