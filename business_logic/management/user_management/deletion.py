from core.management.deletion import Deleter
from auth_app.models import User

class UserDeleter(Deleter):
    
    def delete(self, instance_id):
        return User.objects.delete(id=instance_id)
