from ._weight_converters._factories import *

class ConverterFactory():

    def _create_converter(self, quantity, convert_from, convert_to):
        _converter_factory = None

        if quantity == 'weight':
            _converter_factory = WeightConverterFactory().create_converter(convert_from, convert_to)
            return _converter_factory

        return _converter_factory

    def create_converter(self, quantity, convert_from, convert_to):
        return self._create_converter(quantity, convert_from, convert_to)

