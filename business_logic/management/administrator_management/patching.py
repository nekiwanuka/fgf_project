from core.management.patching import Patcher
from auth_app.models import Administrator

class AdministratorPatcher(Patcher):
    
    def  patch(self, instance, validated_data: dict) -> object:
        for [key, value] in validated_data:
            instance[key] = instance[value]
        return instance.save()
