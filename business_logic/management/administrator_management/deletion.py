from core.management.deletion import Deleter
from auth_app.models import Administrator

class AdministratorDeleter(Deleter):
    
    def delete(self, instance_id):
        return Administrator.objects.delete(id=instance_id)
