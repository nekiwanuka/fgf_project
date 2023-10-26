from core.management.deletion import Deleter
from api.models import Organization

class OrganizationDeleter(Deleter):
    
    def delete(self, instance_id):
        return Organization.objects.delete(id=instance_id)
