from core.management.deletion import Deleter
from auth_app.models import Contributor

class ContributorDeleter(Deleter):
    
    def delete(self, instance_id):
        return Contributor.objects.delete(id=instance_id)
