from auth_app.models import User
#from auth_app.serializers import (UserProfileSerializer, UpdateUserProfileSerializer)
from core.mixins import view_mixins
from core.utilities.rest_exceptions import (PermissionDenied)
from business_logic.auth.permissions import HasUserGroup


# Create your views here.

def _get_queryset(view_instance):
    try:
        user = view_instance.request.user
        if user:
            return User.objects.all().filter(Id=user.Id)
        raise PermissionDenied()
    except Exception as exception:
        raise exception





# class CreateUserViewSet(view_mixins.BaseCreateAPIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = CreateUserSerializer
#     lookup_field = 'id'

#     def post(self, request):
#         try:
#             return self.create(request)
#         except Exception as exception:
#             raise exception


class ViewUsersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    #serializer_class = UserProfileSerializer
    lookup_field = 'Id'
    #filter_backends = [filters.SearchFilter]
    search_fields = ['user']

    def get(self, request):
        if 'user' in cache:
            # get results from cache
            user = cache.get('user')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [vehicle.to_json() for vehicle in queryset]
            # store data in cache
            cache.set('user', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveAuthenticatedUserProfileViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    #serializer_class = UserProfileSerializer
    lookup_field = 'Id'
    permission_classes = [HasUserGroup]

    def get_queryset(self):
        return _get_queryset(self)


class UpdateAuthenticatedUserProfileViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    #serializer_class = UpdateUserProfileSerializer
    permission_classes = [HasUserGroup]
    lookup_field = 'id'

    def get_queryset(self):
        return _get_queryset(self)


# class DeleteUserViewSet(view_mixins.BaseDeleteAPIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'id'

#     def delete(self, request, id=None):
#         try:
#             return self.destroy(request, id)
#         except Exception as exception:
#             raise exception


# class UserLoginView(generics.GenericAPIView):
#     serializer_class = UserLoginSerializer
#     permission_classes = []

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         if serializer.is_valid():
#             data = serializer.validated_data
#             return Response(data=data, status=status.HTTP_200_OK)

