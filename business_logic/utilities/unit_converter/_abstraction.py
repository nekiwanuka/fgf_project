from abc import ABC, abstractmethod

# Abstract type for all measurement Quantity converters.
class AbstractConverter(ABC):

    # Data / Attributes
    _measurement_quantities      = ['weight','volume', 'currency']
    _measurement_units           = []
    _measurement_quantity:str    = None
    _convert_from:str            = None
    _convert_to:str              = None
    _value:float                 = None

    def _set_measurement_quantity(self, measurement_quantity:str):
        if (measurement_quantity in self.get_measurement_quantities()):
            self._measurement_quantity = measurement_quantity
        else:
            raise 'invalid measurement quantity specified!'

    def set_measurement_quantity(self, measurement_quantity:str):
        self._set_measurement_quantity(measurement_quantity)

    def set_measurement_units(self, measurement_units:list):
        self._measurement_units = measurement_units


    def _set_convert_from(self, convert_from:str):
        if (convert_from in self.get_measurement_units()):
            self._convert_from = convert_from
        else:
            raise 'invalid measurement unit specified for convert_from!'

    def set_convert_from(self, convert_from:str):
        self._set_convert_from(convert_from)


    def _set_convert_to(self, convert_to:str):
        if (convert_to in self.get_measurement_units()):
            self._convert_to = convert_to
        else:
            raise 'invalid measurement unit specified for convert_to!'

    def set_convert_to(self, convert_to:str):
        self._set_convert_to(convert_to)

    def set_value(self, value:float):
        self._value = value


    def _set_all_data(self, measurement_quantity:str, convert_from:str, convert_to:str, value:float):
        self.set_measurement_quantity(measurement_quantity)
        self.set_convert_from(convert_from)
        self.set_convert_to(convert_to)
        self.set_value(value)

    def set_all_data(self, measurement_quantity:str, convert_from:str, convert_to:str, value:float):
        self._set_all_data(measurement_quantity, convert_from, convert_to, value)


    def get_measurement_quantities(self):
        return self._measurement_quantities

    def get_measurement_units(self):
        return self._measurement_units

    def get_measurement_quantity(self):
        return self._measurement_quantity

    def get_convert_from(self):
        return self._convert_from

    def get_convert_to(self):
        return self._convert_to

    def get_value(self):
        return self._value


    def _get_all_data(self):
        return {
                self.get_measurement_quantity(),
                self.get_measurement_units(),
                self.get_convert_from(),
                self.get_convert_to(),
                self.get_value(),
            }

    def get_all_data(self):
        self._get_all_data()

    @abstractmethod
    def convert(self):
        pass
