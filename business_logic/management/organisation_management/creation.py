from core.management.creation import Creator
from api.models import Organization

class OrganizationCreator(Creator):
    
    def  create(self, validated_data: dict) -> object:
        return Organization.objects.create(validated_data)
