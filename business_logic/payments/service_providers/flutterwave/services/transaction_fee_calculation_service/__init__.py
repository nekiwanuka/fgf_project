from .__abstraction import AbstractTransactionFeeCalculator as AbstractTransactionFeeCalculator
from .__factories import MainCategoryBasedCalculatorFactory

class FlutterwaveTransactionFeeCalculator(AbstractTransactionFeeCalculator):
    
    def __calculate_transaction_fee(self, request:dict) -> float:
        __amount = float(request['amount'])
        __calculator = MainCategoryBasedCalculatorFactory().create(request)
        __transaction_fee = __calculator.calculate_transaction_fee(__amount)
        return __transaction_fee

    def calculate_transaction_fee(self, request:dict) -> float:
        return self.__calculate_transaction_fee(request)
