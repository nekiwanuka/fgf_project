from core.management import AbstractManager

from .creation import ContributorCreator as Creator
from .list_viewing import ContributorListViewer as ListViewer
from  .retrieval import ContributorRetriever as Retriever
from .updating import ContributorUpdater as Updater
from .patching import ContributorPatcher as Patcher
from .deletion import ContributorDeleter as Deleter

class ContributorManager(AbstractManager):

    def __init__(self) -> None:
        super().__init__()
        self.set_creator(Creator())
        self.set_list_viewer(ListViewer())
        self.set_retriever(Retriever())
        self.set_updater(Updater())
        self.set_patcher(Patcher())
        self.set_deleter(Deleter())
