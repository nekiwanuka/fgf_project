from ._factories import ConverterFactory

def __converter(quantity, convert_from, convert_to, value):
    _converter = ConverterFactory().create_converter(quantity, convert_from, convert_to)
    _converted_value = _converter.convert(value)
    return _converted_value

def converter(quantity, convert_from, convert_to, value):
    """
        Astandard Library for conversions...
    """
    return __converter(quantity, convert_from, convert_to, value)