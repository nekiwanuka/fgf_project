from core.management.list_viewing import ListViewer
from auth_app.models import Administrator

class AdministratorListViewer(ListViewer):
    
    def get_list(self):
        return Administrator.objects.all()
