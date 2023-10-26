from core.management.retrieval import Retriever
from auth_app.models import Contributor


class ContributorRetriever(Retriever):

    def retrieve(self, instance_id) -> object:
        instance = Contributor.objects.get(id=instance_id)
        return instance
