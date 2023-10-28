import auth_app._views.user_views as views
from django.urls import path
#from fgf import urls as api_urls
from django.conf.urls import include


urlpatterns = [
    #path("account/signup/",
    #    views.CreateUserViewSet.as_view({'post': 'create'})),
    # path('', views.ViewUsersListViewSet.as_view(
    #     {'get': 'list'}), name="view_user"),
    # path(r'<str:Id>/', views.RetrieveUserViewSet.as_view(
    #     {'get': 'retrieve'}), name="retrieve_user"),
    
    #Commented out for now
    # path('authenticated-user/addresses/', include(api_urls.useraddress_urls)),
    # path('authenticated-user/emailaddresses/', include(api_urls.useremailaddress_urls)), #TD
    # path('authenticated-user/phonenumbers/', include(api_urls.userphonenumber_urls)), #TD
    # path('authenticated-user/socialaccounts/', include(api_urls.usersocialaccount_urls)), #TD
    # path('authenticated-user/websites/', include(api_urls.userwebsite_urls)), #TD
    # path('authenticated-user/photos/', include(api_urls.userphoto_urls)),
    path('authenticated-user/<str:Id>/profile/', views.RetrieveAuthenticatedUserProfileViewSet.as_view(
        {'get': 'retrieve'}), name="retrive user profile"),
    path('authenticated-user/<str:Id>/profile/update/', views.UpdateAuthenticatedUserProfileViewSet.as_view(
        {'put': 'update'}), name="update user profile"),
]
