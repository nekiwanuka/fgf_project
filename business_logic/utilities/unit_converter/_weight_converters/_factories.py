from . import *

class WeightConverterFactory():

    def _create_converter(self, convert_from, convert_to):
        _weight_converter_factory = None

        if convert_to == 'kilogram':
            _weight_converter_factory = ToKilogramConverterFactory().create_converter(convert_from)

        return _weight_converter_factory

    def create_converter(self, convert_from, convert_to):
        return self._create_converter(convert_from, convert_to)

