from abc import abstractmethod
from .._abstraction import *

class AbstractWeightConverter(AbstractConverter):

    def _init(self):
        self.set_measurement_quantity()
        self.set_measurement_units()

    def __init__(self):
        self._init()

    def _set_measurement_quantity(self):
        super().set_measurement_quantity('weight')

    def set_measurement_quantity(self):
        self._set_measurement_quantity()

    def _set_measurement_units(self):
        super().set_measurement_units(['gram', 'milligram', 'kilogram', 'tonne', 'ounce', 'pound'])

    def set_measurement_units(self):
        self._set_measurement_units()

    @abstractmethod
    def convert():
        pass
