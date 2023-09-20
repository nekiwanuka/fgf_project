from django.urls import path
from . import views

urlpatterns = [
    path('cultures/', views.Cultural_IdentityListview.as_view()),
    path('cultures/<int:pk>/', views.Cultural_IdentityDetailView.as_view()),
    path('cultures/cultural_kingdom/', views.Cultural_KingdomListview.as_view()),
    path('cultures/cultural_kingdom/<int:pk>/', views.Cultural_KingdomDetailView.as_view()),
    path('cultures/ethnicities/', views.EthnicityListview.as_view()),
    path('cultures/ethnicities/<int:pk>/', views.EthnicityDetailView.as_view()),
    path('cultures/clans/', views.ClanListview.as_view()),
    path('cultures/clans/<int:pk>/', views.ClanDetailView.as_view()),
    path('cultures/ethnic_groups/', views.Ethnic_GroupListview.as_view()),
    path('cultures/ethnic_groups/<int:pk>/', views.Ethnic_GroupDetailView.as_view()),
     
]

