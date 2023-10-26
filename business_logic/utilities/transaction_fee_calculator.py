from ..payments.service_providers.flutterwave.adapters import FlutterwaveTransactionFeeCalculationAdapter

def __payments_gateway_adapter_factory(payments_gateway:str):
    __payments_gateway_adapter = None

    if payments_gateway == 'flutterwave':
        __payments_gateway_adapter = FlutterwaveTransactionFeeCalculationAdapter()
    
    return __payments_gateway_adapter

def __get_transaction_fee(request:dict) -> float:
    __payments_gateway_adapter = __payments_gateway_adapter_factory(request['payment_gateway'])
    return __payments_gateway_adapter.get_transaction_fee(request)

def get_transaction_fee(request:dict) -> float:
    return __get_transaction_fee(request)
