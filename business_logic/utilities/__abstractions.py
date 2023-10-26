from abc import ABC, abstractmethod

class TransactionFeeCalculator(ABC):
    
    @abstractmethod
    def get_transaction_fee(request:dict) -> float:
        pass

