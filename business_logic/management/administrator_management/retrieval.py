from core.management.retrieval import Retriever
from auth_app.models import Administrator


class AdministratorRetriever(Retriever):

    def retrieve(self, instance_id) -> object:
        instance = Administrator.objects.get(id=instance_id)
        return instance
