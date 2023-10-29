from abc import ABC as AbstractClass

from business_logic.user_accounts import UserAccountsController
from business_logic.auth import AuthController

# EmailAndPasswordAuthentication

class AbstractUser(AbstractClass):
    """
    A controller for the system user.
    """
    _profile_controller = None
    _accounts_controller = None
    _organizations_controller = None
    _orders_controller = None
    _payments_controller = None
    _auth_controller = None

    # Mutators
    def set_profile_controller(self, profile_controller):
        self._profile_controller = profile_controller

    def set_accounts_controller(self, accounts_controller):
        self._accounts_controller = accounts_controller

    def set_organizations_controller(self, organizations_controller):
        self._organizations_controller = organizations_controller

    def set_orders_controller(self, orders_controller):
        self._orders_controller = orders_controller

    def set_payments_controller(self, payments_controller):
        self._payments_controller = payments_controller

    def set_auth_controller(self, auth_controller):
        self._auth_controller = auth_controller

    # Accessors
    def get_profile_controller(self):
        return self._profile_controller

    def get_accounts_controller(self):
        return self._accounts_controller

    def get_organizations_controller(self):
        return self._organizations_controller

    def get_orders_controller(self):
        return self._orders_controller

    def get_payments_controller(self):
        return self._payments_controller

    def get_auth_controller(self):
        return self._auth_controller


class User(AbstractUser):
    # Generic User Operations
    def register_user(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_user(request)

    def register_staff(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_staff(request)

    def register_vendor(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_vendor(request)

    def register_client(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_client(request)

    def register_courier(self, request):
        self.set_accounts_controller(UserAccountsController())
        return self.get_accounts_controller().register_courier(request)

    def login(self, login_data):
        self.set_auth_controller(AuthController())
        return self.get_auth_controller().in_logger.login(login_data)

