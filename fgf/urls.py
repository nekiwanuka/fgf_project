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