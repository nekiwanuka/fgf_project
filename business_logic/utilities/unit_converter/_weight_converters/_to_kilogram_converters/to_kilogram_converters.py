from . import AbstractToKilogramWeightConverter

class MilligramToKilogramWeightConverter(AbstractToKilogramWeightConverter):
    
    def __init__(self):
        super()

    def __convert(self, value):
        weight_in_kg = value/1000000
        return weight_in_kg

    def convert(self, value):
        return self.__convert(value)


class GramToKilogramWeightConverter(AbstractToKilogramWeightConverter):
    
    def __init__(self):
        super()

    def __convert(self, value):
        weight_in_kg = round(value/1000, 5)
        return weight_in_kg

    def convert(self, value):
        return self.__convert(value)


class TonneToKilogramWeightConverter(AbstractToKilogramWeightConverter):
    
    def __init__(self):
        super()

    def __convert(self, value):
        weight_in_kg = round(value*1000, 5)
        return weight_in_kg

    def convert(self, value):
        return self.__convert(value)


class OunceToKilogramWeightConverter(AbstractToKilogramWeightConverter):
        
    def __init__(self):
        super()

    def __convert(self, value):
        weight_in_kg =round(value/35.27396, 5)
        return weight_in_kg

    def convert(self, value):
        return self.__convert(value)
   

class PoundToKilogramWeightConverter(AbstractToKilogramWeightConverter):

        
    def __init__(self):
        super()

    def __convert(self, value):
        weight_in_kg = round(value/2.204623, 5)
        return weight_in_kg

    def convert(self, value):
        return self.__convert(value)
