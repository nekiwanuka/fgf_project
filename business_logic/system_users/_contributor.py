from . import _user
from business_logic.auth import AuthController
from business_logic.auth.authentication import ContributorEmailAndPasswordAuthentication

User = _user.User

class Contributor(User):
    """
    A controller for Contributor as a system user.
    """
    def __init__(self,):
        super()

    # Mutators

    # Accessors 

    # Generic User Operations
    def login(self, login_data):
        self.set_auth_controller(AuthController())
        self.get_auth_controller().set_in_logger(ContributorEmailAndPasswordAuthentication())
        InLogger = self.get_auth_controller().get_in_logger()
        return InLogger.login(login_data)
