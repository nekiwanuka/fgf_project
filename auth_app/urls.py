from django.urls import path
from .views import UserListCreateView, UserDetailView, \
    AdministratorListCreateView, AdministratorDetailView, \
    ContributorListCreateView, ContributorDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('administrators/', AdministratorListCreateView.as_view(), name='administrator-list'),
    path('administrators/<uuid:pk>/', AdministratorDetailView.as_view(), name='administrator-detail'),
    path('contributors/', ContributorListCreateView.as_view(), name='contributor-list'),
    path('contributors/<uuid:pk>/', ContributorDetailView.as_view(), name='contributor-detail'),
]
