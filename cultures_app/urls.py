from django.urls import path
from . import views

urlpatterns = [
    
    #path('api/cultures/', views.CulturalIdentityListCreateView.as_view(), name='culture-list-create'),
    #path('cultures/<int:pk>/', views.CulturalIdentityDetailView.as_view()),
    
    path('api/cultures/clans/', views.ClanListView.as_view()),
    path('api/cultures/clans/<int:pk>/', views.ClanDetailView.as_view()),
    
    path('api/cultures/cultural_kingdom/', views.CulturalKingdomListView.as_view()),
    path('api/cultures/cultural_kingdom/<int:pk>/', views.CulturalKingdomDetailView.as_view()),
    
    path('api/cultures/ethnicities/', views.EthnicityListView.as_view()),
    path('api/cultures/ethnicities/<int:pk>/', views.EthnicityDetailView.as_view()),
    
    path('api/cultures/', views.EthnicGroupListView.as_view(), name='culture-list-create'),
    path('api/cultures/<int:pk>/', views.EthnicGroupDetailView.as_view()),
     
]

