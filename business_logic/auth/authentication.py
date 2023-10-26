"""
    Check login credentials to see if you recognize a user trying to login
"""

from abc import ABC as AbstractClass
from business_logic.management.administrator_management import AdministratorManager
from business_logic.management.contributor_management import ContributorManager

from  core.auth.authentication import  EmailAndPasswordAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone

class UserAuthentication(AbstractClass):
    _auth_type = None

    def set_auth_type(self, auth_type):
        self._auth_type = auth_type

    def get_auth_type(self):
        return self._auth_type

    def user_login(self, login_data):
        auth = self.get_auth_type()
        is_authenticated = auth.is_authenticated(login_data)
        if is_authenticated:
            user = auth.get_user()
            return user

class AdministratorEmailAndPasswordAuthentication(UserAuthentication):

    def login(self, login_data):
        try:
            self.set_auth_type(EmailAndPasswordAuthentication())
            user = self.user_login(login_data)
            administrator_count = AdministratorManager().get_list().filter(user=user).count() or 0
            if administrator_count<1:
                raise AuthenticationFailed('Invalid Credentials, Possibly you are not registered as an Administrator.')
            administrator = AdministratorManager().get_list().filter(user=user)[0]
            return_object = {
                'login_status': 'success',
                'email': user.email,
                'user_id': user.Id,
                'tokens': user.tokens()
            }
            return_object['administrator_id'] = administrator.id
            user.last_login = timezone.now()
            user.save()
            return return_object
        except Exception as exception:
            raise exception

class ContributorEmailAndPasswordAuthentication(UserAuthentication):

    def login(self, login_data):
        try:
            self.set_auth_type(EmailAndPasswordAuthentication())
            user = self.user_login(login_data)
            contributor_count = ContributorManager().get_list().filter(user=user).count() or 0
            if contributor_count<1:
                raise AuthenticationFailed('Invalid Credentials, Possibly you have not yet signed up as a Contributor.')
            contributor = ContributorManager().get_list().filter(user=user)[0]
            return_object = {
                'login_status': 'success',
                'email': user.email,
                'user_id': user.Id,
                'tokens': user.tokens()
            }
            return_object['contributor_id'] = contributor.id
            user.last_login = timezone.now()
            user.save()
            return return_object
        except Exception as exception:
            raise exception
