"""
from django.urls import path, re_path, include
from django.contrib import admin
from auth_app._urls import user_urls as user_urls
from auth_app._urls import administrator_urls as administrator_urls
from auth_app._urls import contributor_urls as contributor_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Name",
        default_version="v1",
        description="Description of your API",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
)
# YASG-related routes
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('users/', include(user_urls)),
    path('administrators/', include(administrator_urls)),
    path('contributors/', include(contributor_urls)),
    #path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    #path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
"""

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

from django.conf import settings
#from django.conf.urls import include

from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions, routers
# from authentication.views import VerifyEmail,  RegisterView
#from api import urls as api_urls
from auth_app._urls import user_urls as user_urls
from auth_app._urls import administrator_urls as administrator_urls
from auth_app._urls import contributor_urls as contributor_urls

#from drf_spectacular.extensions import OpenApiAuthenticationExtension
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework_simplejwt import views as jwt_views

# from rest_framework.urlpatterns import format_suffix_patterns

# schema_view = get_schema_view(
#     openapi.Info(
#         title="FGF API Official Documentation",
#         default_version='v1',
#         description="FGF API description",
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     #permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
# )
# End: drf_yasg

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()

urlpatterns = [
    # Default route
    #path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Admin route
    re_path(r'^admin/', admin.site.urls),

    # User and Account Routes
    #path('account/', include(auth_app)),
    path('users/', include(user_urls)),
    path('administrators/', include(administrator_urls)),
    path('contributors/', include(contributor_urls)),

    # api routes
    # drf-yasg Routes - PK Comment
    # path('docs/swagger/', schema_view.with_ui('swagger',
    #      cache_timeout=0), name='schema-swagger-ui'),
    # path('docs/redoc/', schema_view.with_ui('redoc',
    #      cache_timeout=0), name='schema-redoc'),

    # categories
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    path('api-auth/', include('rest_framework.urls')),
    
    path('api/plants/', include('plants_app.urls'), name='plants'),
    path('api/animals/', include('animals_app.urls'), name='animals'),
    path('api/cultures/', include('cultures_app.urls'), name='cultures'),
    #path('', include('auth_app.urls'), name='auth'),
    
    #path('auth_app/', include('rest_authtoken.urls')),
    path('', include('animals_app.urls'), name='animals'), 
    path('', include('cultures_app.urls'), name='cultures'),
    path('', include('plants_app.urls'), name='plants'), 
    
] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)