import auth_app._views.administrator_views as views
from django.urls import path


urlpatterns = [
    path('', views.ViewAdministratorsListViewSet.as_view(
        {'get': 'list'}), name="view_administrator"),
    path(r'<str:id>/', views.RetrieveAdministratorViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_administrator"),
    # path(r'<str:id>/update/',
    #      views.UpdateAdministratorViewSet.as_view({'put': 'update'})),
    # path(r'<str:id>/delete/',
    #      views.DeleteAdministratorViewSet.as_view({'delete': 'destroy'})),
    path(r'account/login/',
         views.AdministratorLoginView.as_view()),
]
