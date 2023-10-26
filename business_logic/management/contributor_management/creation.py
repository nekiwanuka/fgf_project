from core.management.creation import Creator
from auth_app.models import Contributor

class ContributorCreator(Creator):
    
    def  create(self, validated_data: dict) -> object:
        user = validated_data.get('user')
        contributor = Contributor.objects.create(user=user)
        return contributor
