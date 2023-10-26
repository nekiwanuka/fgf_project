from core.management import AbstractManager

from .creation import OrganizationCreator as Creator
from .list_viewing import OrganizationListViewer as ListViewer
from  .retrieval import OrganizationRetriever as Retriever
from .updating import OrganizationUpdater as Updater
from .patching import OrganizationPatcher as Patcher
from .deletion import OrganizationDeleter as Deleter

class OrganizationManager(AbstractManager):
    
    def __init__(self) -> None:
        super().__init__()
        self.set_creator(Creator())
        self.set_list_viewer(ListViewer())
        self.set_retriever(Retriever())
        self.set_updater(Updater())
        self.set_patcher(Patcher())
        self.set_deleter(Deleter())
