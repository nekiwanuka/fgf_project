from core.management.creation import Creator
from auth_app.models import Administrator

class AdministratorCreator(Creator):
    
    def  create(self, validated_data: dict) -> object:
        user = validated_data.get('user')
        administrator = Administrator.objects.create(user=user)
        return administrator
