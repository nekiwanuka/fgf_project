from abc import ABC, abstractmethod

# Abstract type for all measurement Quantity converters.
class Converter(ABC):

    # Data / Attributes
    _measurement_quantities      = ['weight','volume', 'currency']
    _measurement_units           = []
    _measurement_quantity:str    = None
    _convert_from:str            = None
    _convert_to:str              = None
    _value:float                 = None

    def set_measurement_quantity(self, measurement_quantity:str):
        if (measurement_quantity in self.get_measurement_quantities()):
            self._measurement_quantity = measurement_quantity
        else:
            raise 'invalid measurement quantity specified!'

    def set_measurement_units(self, measurement_units:list):
        self._measurement_units = measurement_units

    def set_convert_from(self, convert_from:str):
        if (convert_from in self.get_measurement_units()):
            self._convert_from = convert_from
        else:
            raise 'invalid measurement unit specified for convert_from!'

    def set_convert_to(self, convert_to:str):
        if (convert_to in self.get_measurement_units()):
            self._convert_to = convert_to
        else:
            raise 'invalid measurement unit specified for convert_to!'

    def set_value(self, value:float):
        self._value = value

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

    def set_all_data(self, measurement_quantity:str, convert_from:str, convert_to:str, value:float):
        self.set_measurement_quantity(measurement_quantity)
        self.set_convert_from(convert_from)
        self.set_convert_to(convert_to)
        self.set_value(value)

    def get_all_data(self):
        return {
                self.get_measurement_quantity(),
                self.get_measurement_units(),
                self.get_convert_from(),
                self.get_convert_to(),
                self.get_value(),
            }

    @abstractmethod
    def convert(self):
        pass


class WeightConverter(Converter):
    def __init__(self):
        self.set_measurement_quantity()
        self.set_measurement_units()

    def set_measurement_quantity(self):
        super().set_measurement_quantity('weight')

    def set_measurement_units(self):
        super().set_measurement_units(['gram', 'milligram', 'kilogram', 'tonne', 'ounce', 'pound'])

    @abstractmethod
    def convert():
        pass


class ToKilogramWeightConverter(WeightConverter):

    def __init__(self):
        self.set_convert_to()
        super()

    def set_convert_to(self):
        super().set_measurement_units()
        super().set_convert_to('kilogram')

    @abstractmethod
    def convert():
        pass


class MilligramToKilogramWeightConverter(ToKilogramWeightConverter):

    def __init__(self):
        self.set_convert_from()
        super()

    def set_convert_from(self):
        super().set_measurement_units()
        super().set_convert_to()
        super().set_convert_from('milligram')


    def _convert(self, value):
        weight_in_kg = value/1000000
        return weight_in_kg

    def convert(self, value):
        return self._convert(value)


class GramToKilogramWeightConverter(ToKilogramWeightConverter):
    
    def __init__(self):
        self.set_convert_from()
        super()

    def set_convert_from(self):
        super().set_measurement_units()
        super().set_convert_to()
        super().set_convert_from('gram')


    def _convert(self, value):
        weight_in_kg = round(value/1000, 5)
        return weight_in_kg

    def convert(self, value):
        return self._convert(value)


class TonneToKilogramWeightConverter(ToKilogramWeightConverter):
    
    def __init__(self):
        self.set_convert_from()
        super()

    def set_convert_from(self):
        super().set_measurement_units()
        super().set_convert_to()
        super().set_convert_from('tonne')


    def _convert(self, value):
        weight_in_kg = round(value*1000, 5)
        return weight_in_kg

    def convert(self, value):
        return self._convert(value)


class OunceToKilogramWeightConverter(ToKilogramWeightConverter):
    
    def __init__(self):
        self.set_convert_from()
        super()

    def set_convert_from(self):
        super().set_measurement_units()
        super().set_convert_to()
        super().set_convert_from('ounce')


    def _convert(self, value):
        weight_in_kg =round(value/35.27396, 5)
        return weight_in_kg

    def convert(self, value):
        return self._convert(value)
    

class PoundToKilogramWeightConverter(ToKilogramWeightConverter):

    def __init__(self):
        self.set_convert_from()
        super()

    def set_convert_from(self):
        super().set_measurement_units()
        super().set_convert_to()
        super().set_convert_from('pound')


    def _convert(self, value):
        weight_in_kg = round(value/2.204623, 5)
        return weight_in_kg

    def convert(self, value):
        return self._convert(value)
    

# converter = MilligramToKilogramWeightConverter()
# print(converter.convert(1000))
# converter = GramToKilogramWeightConverter()
# print(converter.convert(1000))
# converter = TonneToKilogramWeightConverter()
# print(converter.convert(1000))
# converter = OunceToKilogramWeightConverter()
# print(converter.convert(1000))
# converter = PoundToKilogramWeightConverter()
# print(converter.convert(1000))

