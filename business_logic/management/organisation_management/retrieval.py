from core.management.retrieval import Retriever
from api.models import Organization


class OrganizationRetriever(Retriever):

    def retrieve(self, instance_id) -> object:
        instance = Organization.objects.get(id=instance_id)
        return instance
