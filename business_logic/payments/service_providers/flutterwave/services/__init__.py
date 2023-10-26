from .transaction_fee_calculation_service import FlutterwaveTransactionFeeCalculator as FlutterwaveTransactionFeeCalculator

def calculate_transaction_fee(request:dict) -> float:
    return FlutterwaveTransactionFeeCalculator().calculate_transaction_fee(request)
