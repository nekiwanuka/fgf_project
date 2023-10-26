from core.management.list_viewing import ListViewer
from auth_app.models import User

class UserListViewer(ListViewer):
    
    def get_list(self):
        return User.objects.all()
