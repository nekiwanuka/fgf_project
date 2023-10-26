from core.management import AbstractManager

from .creation import AdministratorCreator as Creator
from .list_viewing import AdministratorListViewer as ListViewer
from  .retrieval import AdministratorRetriever as Retriever
from .updating import AdministratorUpdater as Updater
from .patching import AdministratorPatcher as Patcher
from .deletion import AdministratorDeleter as Deleter

class AdministratorManager(AbstractManager):

    def __init__(self) -> None:
        super().__init__()
        self.set_creator(Creator())
        self.set_list_viewer(ListViewer())
        self.set_retriever(Retriever())
        self.set_updater(Updater())
        self.set_patcher(Patcher())
        self.set_deleter(Deleter())
