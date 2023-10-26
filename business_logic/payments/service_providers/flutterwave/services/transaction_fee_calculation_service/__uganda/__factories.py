from ..__abstraction import AbstractFactory as AbstractFactory
from .__payment import PaymentCategoryBasedCalculatorFactory

class MainCategoryBasedCalculatorFactory(AbstractFactory):

    def __create(self, request:dict):
        __calculator:AbstractFactory = None
        __main_category = request['main_category']

        if (__main_category == 'payment'):
            __calculator = PaymentCategoryBasedCalculatorFactory().create(request)

        return __calculator

    def create(self, request:dict):
        return self.__create(request)
