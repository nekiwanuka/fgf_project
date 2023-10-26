from .__abstraction import AbstractFactory as AbstractFactory
from .__uganda import MainCategoryBasedCalculatorFactory

class CountryBasedCalculatorFactory(AbstractFactory):

    def __create(self, country:str, main_category:str, category:str):
        __calculator:AbstractFactory = None

        if (country == 'uganda'):
            __calculator = MainCategoryBasedCalculatorFactory().create(main_category, category)

        return __calculator

    def create(self, country:str, main_category:str, category:str):
        return self.__create(country, main_category, category)
