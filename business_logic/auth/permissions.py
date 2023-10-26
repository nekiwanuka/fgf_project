from rest_framework.permissions import BasePermission, IsAuthenticated
#from api.models import (CourierOrganization, Organization, VendorOrganization)
from core.utilities.rest_exceptions import (PermissionDenied, AuthenticationFailed)
from auth_app.models import *


# class IsAuthenticated(IsAuthenticated):
#     pass


class HasUserGroup(BasePermission):
    """
    Gives access to Grouped Users.
    """

    message = 'Operation not allowed. Either the user-group field was not specified in the request Header or the current user does not belong to the specified user-group.'

    def has_permission(self, request, view):
        permit = False
        group = request.META.get('HTTP_USER_GROUP')
        permit = bool(group is not None and ( (group == 'administrator') or (group == 'staff') or (group == 'contributor')))
        if group == 'administrator':
            permit = bool(Administrator.objects.all().filter(user=request.user).exists())
        if group == 'contributor':
            permit = bool(Contributor.objects.all().filter(user=request.user).exists())
        return permit


class IsAdministrator(BasePermission):
    """
    Gives access to Administrators.
    """

    def has_permission(self, request, view):
        admin = bool(Administrator.objects.filter(user = request.user).exists())
        return bool(IsAuthenticated and admin)


class IsContributor(BasePermission):
    """
    Gives access to Contributor Members
    """

    def has_permission(self, request, view):
        contributor = bool(Contributor.objects.filter(user = request.user).exists())
        return bool(IsAuthenticated and contributor)


def is_administrator(request):
    group = request.META.get('HTTP_USER_GROUP')
    admin = bool(Administrator.objects.filter(user = request.user).exists())
    return bool(IsAuthenticated and admin and (group == 'admin'))


def is_contributor(request):
    group = request.META.get('HTTP_USER_GROUP')
    contributor = bool(Contributor.objects.filter(user = request.user).exists())
    return bool(IsAuthenticated and contributor and (group == 'contributor'))

""" def is_organization(organization_id):
        _organizations = Organization.objects.filter(id=organization_id)
        if not _organizations.exists():
            raise AuthenticationFailed(
                    {
                    "detail": "Authentication failed: invalid organization_id passed in query string."
                    }
                )
        return True """
