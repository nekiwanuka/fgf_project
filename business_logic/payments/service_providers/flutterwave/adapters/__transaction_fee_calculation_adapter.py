from business_logic.utilities.__abstractions import TransactionFeeCalculator
from ..services import FlutterwaveTransactionFeeCalculator

class FlutterwaveTransactionFeeCalculationAdapter(TransactionFeeCalculator):
    def get_transaction_fee(self, request:dict):
        return FlutterwaveTransactionFeeCalculator().calculate_transaction_fee(request)
