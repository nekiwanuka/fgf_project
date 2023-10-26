from .to_kilogram_converters import *

class ToKilogramConverterFactory():

    def _create_converter(self, convert_from):
        _to_kilogram_converter_factory = None

        if convert_from == 'milligram':
            _to_kilogram_converter_factory = MilligramToKilogramWeightConverter()

        if convert_from == 'gram':
            _to_kilogram_converter_factory = GramToKilogramWeightConverter()

        if convert_from == 'tonne':
            _to_kilogram_converter_factory = TonneToKilogramWeightConverter()

        if convert_from == 'ounce':
            _to_kilogram_converter_factory = OunceToKilogramWeightConverter()

        if convert_from == 'pound':
            _to_kilogram_converter_factory = PoundToKilogramWeightConverter()

        # _to_kilogram_converter_factory.set_convert_from(convert_from)
        return _to_kilogram_converter_factory

    def create_converter(self, convert_from):
        return self._create_converter(convert_from)
