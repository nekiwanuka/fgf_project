from .... import AbstractTransactionFeeCalculator

class MobileMoneyTransactionFeeCalculator(AbstractTransactionFeeCalculator):
    
    def __calculate_transaction_fee(self, amount) -> float:
        __amount = float(amount)
        __transaction_fee = 0.0

        if (__amount + 200) in range(1, 5000):
            __transaction_fee = 200

        elif (__amount + 700) in range(5000, 30001):
            __transaction_fee = 700

        elif (__amount + (__amount * 0.03)) >30000:
            __transaction_fee = __amount * 0.03

        else:
            raise ("Invalid amount")

        return __transaction_fee

    def calculate_transaction_fee(self, amount) -> float:
        return self.__calculate_transaction_fee(amount)
