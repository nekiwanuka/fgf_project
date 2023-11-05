import auth_app._views.contributor_views as views
from django.urls import path


urlpatterns = [
    path('account/signup/',
         views.CreateContributorViewSet.as_view({'post': 'create'}), name="signup"),
     #path("account/signup/",
     #    views.CreateContributorViewSet.as_view({'post': 'create'})),    
    path('', views.ViewContributorsListViewSet.as_view(
        {'get': 'list'}), name="view_administrator"),
    path('<str:id>/', views.RetrieveContributorViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_administrator"),
    path('<str:id>/update/',
         views.UpdateContributorViewSet.as_view({'put': 'update'})),
    path('<str:id>/delete/',
         views.DeleteContributorViewSet.as_view({'delete': 'destroy'})),
    path('account/login/',
         views.ContributorLoginView.as_view()),
]
