"""
    Contributor Account Managers
"""
from rest_framework.response import Response
from rest_framework import status

from business_logic.management.contributor_management import ContributorManager
from business_logic.management.user_management import UserManager
from auth_app.serializers import user_serializers
from business_logic.utilities.mailing import EmailVerificationLinkSender
from core.utilities.auth import get_authenticated_user

RegisterUserSerializer = user_serializers.RegisterUserSerializer

class AccountCreator():

    def create(self, request):
        """
        A method for registering a Contributor member
        """
        try:
            validated_data = request['validated_data']
            request = request['request']
            email = validated_data.get('email')
            user_count = UserManager().get_list().filter(email=email).count() or 0
            if user_count<1:
                user = RegisterUserSerializer().create(validated_data)
            user = UserManager().get_list().filter(email=email)[0]
            contributor_count = ContributorManager().get_list().filter(user=user).count() or 0

            if contributor_count>0:
                response_data = {
                        'email': [
                            'Contributor with this email address (' + email + ') already exists.'
                        ]
                    }
                return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.is_contributor = True
                user.save()
                validated_data = {'user':user}
                contributor = ContributorManager().create(validated_data)
                authenticated_user = get_authenticated_user(request)  # or AnonymousUser
                if authenticated_user.__str__() == 'AnonymousUser':
                    authenticated_user = user
                # print(authenticated_user)
                contributor.registered_by = authenticated_user
                contributor.lastupdated_by = authenticated_user
                contributor.save()
                return EmailVerificationLinkSender(request).send()
        except Exception as exception:
            raise exception
