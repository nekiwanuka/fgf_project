from django.urls import path
from . import views

urlpatterns = [
    path('cultures/', views.CulturalIdentityListview.as_view()),
    path('cultures/<int:pk>/', views.CulturalIdentityDetailView.as_view()),
    path('cultures/cultural_kingdom/', views.CulturalKingdomListview.as_view()),
    path('cultures/cultural_kingdom/<int:pk>/', views.CulturalKingdomDetailView.as_view()),
    path('cultures/ethnicities/', views.EthnicityListview.as_view()),
    path('cultures/ethnicities/<int:pk>/', views.EthnicityDetailView.as_view()),
    path('cultures/clans/', views.ClanListview.as_view()),
    path('cultures/clans/<int:pk>/', views.ClanDetailView.as_view()),
    path('cultures/ethnic_groups/', views.EthnicGroupListview.as_view()),
    path('cultures/ethnic_groups/<int:pk>/', views.EthnicGroupDetailView.as_view()),
     
]

