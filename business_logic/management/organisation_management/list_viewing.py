from core.management.list_viewing import ListViewer
from api.models import Organization

class OrganizationListViewer(ListViewer):
    
    def get_list(self) -> list:
        return Organization.objects.all()
