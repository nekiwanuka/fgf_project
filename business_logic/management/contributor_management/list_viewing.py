from core.management.list_viewing import ListViewer
from auth_app.models import Contributor

class ContributorListViewer(ListViewer):
    
    def get_list(self):
        return Contributor.objects.all()
