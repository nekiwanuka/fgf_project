from auth_app.models import Administrator
from auth_app.serializers import (AdministratorSerializer, AdministratorLoginSerializer)
from core.mixins import view_mixins
from rest_framework import generics, status
from rest_framework.response import Response


# Create your views here.
class ViewAdministratorsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    lookup_field = 'id'
    #filter_backends = [filters.SearchFilter]
    search_fields = ['user']

    def get(self, request):
        if 'vehicles' in cache:
            # get results from cache
            vehicles = cache.get('vehicles')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [vehicle.to_json() for vehicle in queryset]
            # store data in cache
            cache.set('vehicles', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveAdministratorViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class AdministratorLoginView(generics.GenericAPIView):
    serializer_class = AdministratorLoginSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            data = serializer.validated_data
            return Response(data=data, status=status.HTTP_200_OK)


# class CreateAdministratorViewSet(view_mixins.BaseCreateAPIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Administrator.objects.all()
#     serializer_class = CreateAdministratorSerializer
#     lookup_field = 'id'

#     def post(self, request):
#         try:
#             return self.create(request)
#         except Exception as exception:
#             raise exception


# class UpdateAdministratorViewSet(view_mixins.BaseUpdateAPIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Administrator.objects.all()
#     serializer_class = AdministratorSerializer
#     lookup_field = 'id'

#     def put(self, request, id=None):
#         try:
#             return self.update(request, id)
#         except Exception as exception:
#             raise exception


# class DeleteAdministratorViewSet(view_mixins.BaseDeleteAPIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Administrator.objects.all()
#     serializer_class = AdministratorSerializer
#     lookup_field = 'id'

#     def delete(self, request, id=None):
#         try:
#             return self.destroy(request, id)
#         except Exception as exception:
#             raise exception


