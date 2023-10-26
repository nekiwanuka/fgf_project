from business_logic.user_accounts._abstract_account_manager import AbstractAccountManager
from ._administrator_account import AccountManager as AdministratorAccountManager
from ._contributor_account import AccountManager as ContributorAccountManager


class UserAccountsController():
    _administrator_account_manager:AbstractAccountManager
    _staff_account_manager:AbstractAccountManager
    _vendor_account_manager:AbstractAccountManager
    _contributor_account_manager:AbstractAccountManager
    _courier_account_manager:AbstractAccountManager

    def set_administrator_account_manager(self, administrator_account_manager):
        self._administrator_account_manager = administrator_account_manager

    def get_administrator_account_manager(self):
        return self._administrator_account_manager

    def set_staff_account_manager(self, staff_account_manager):
        self._staff_account_manager = staff_account_manager

    def get_staff_account_manager(self):
        return self._staff_account_manager

    def set_vendor_account_manager(self, vendor_account_manager):
        self._vendor_account_manager = vendor_account_manager

    def get_vendor_account_manager(self):
        return self._vendor_account_manager

    def set_contributor_account_manager(self, contributor_account_manager):
        self._contributor_account_manager = contributor_account_manager

    def get_contributor_account_manager(self):
        return self._contributor_account_manager

    def set_courier_account_manager(self, courier_account_manager):
        self._courier_account_manager = courier_account_manager

    def get_courier_account_manager(self):
        return self._courier_account_manager

    # Operations
    def register_administrator(self, request):
        self.set_administrator_account_manager(AdministratorAccountManager())
        return self._administrator_account_manager.register_administrator(request)


    def register_contributor(self, request):
        self.set_contributor_account_manager(ContributorAccountManager())
        return self._contributor_account_manager.register_contributor(request)

