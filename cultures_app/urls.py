from django.urls import path
from . import views

urlpatterns = [
    path('cultures/', views.Cultural_KingdomListview.as_view()),
    path('cultures/<int:pk>/', views.Cultural_KingdomDetailView.as_view()),
    path('cultures/tribes/', views.TribeListview.as_view()),
    path('cultures/tribes/<int:pk>/', views.TribeDetailView.as_view()),
    path('cultures/clans/', views.ClanListview.as_view()),
    path('cultures/clans/<int:pk>/', views.ClanDetailView.as_view()),
    path('cultures/identities/', views.Cultural_IdentityListview.as_view()),
    path('cultures/identities/<int:pk>/', views.Cultural_IdentityDetailView.as_view()),
    

]

