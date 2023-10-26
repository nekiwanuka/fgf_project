from abc import abstractmethod
from .._abstraction import *

class AbstractToKilogramWeightConverter(AbstractWeightConverter):

    def _init(self):
        self.set_convert_to()
        super()

    def __init__(self):
        self._init()

    def _set_convert_to(self):
        super().set_measurement_units()
        super().set_convert_to('kilogram')

    def set_convert_to(self):
        self._set_convert_to()

    @abstractmethod
    def convert():
        pass
