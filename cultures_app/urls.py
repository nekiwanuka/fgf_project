from django.urls import path
from . import views

urlpatterns = [
    path('api/cultures/', views.CulturalIdentityListCreateView.as_view(), name='animal-list-create'),
    path('cultures/<int:pk>/', views.CulturalIdentityDetailView.as_view()),
    path('cultures/cultural_kingdom/', views.CulturalKingdomListView.as_view()),
    path('cultures/cultural_kingdom/<int:pk>/', views.CulturalKingdomDetailView.as_view()),
    path('cultures/ethnicities/', views.EthnicityListView.as_view()),
    path('cultures/ethnicities/<int:pk>/', views.EthnicityDetailView.as_view()),
    path('cultures/clans/', views.ClanListView.as_view()),
    path('cultures/clans/<int:pk>/', views.ClanDetailView.as_view()),
    path('cultures/ethnic_groups/', views.EthnicGroupListView.as_view()),
    path('cultures/ethnic_groups/<int:pk>/', views.EthnicGroupDetailView.as_view()),
     
]

