from ...__abstraction import AbstractFactory as AbstractFactory
from .__mobile_money import MobileMoneyTransactionFeeCalculator

class PaymentCategoryBasedCalculatorFactory(AbstractFactory):

    def __create(self, request:dict):
        __calculator = None
        __category = request['payment_category']

        if (__category == 'mobile money'):
            __calculator = MobileMoneyTransactionFeeCalculator()

        return __calculator

    def create(self, request:dict):
        return self.__create(request)
