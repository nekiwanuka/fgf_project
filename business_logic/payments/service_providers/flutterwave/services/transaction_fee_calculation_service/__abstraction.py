from abc import ABC, abstractmethod

class AbstractTransactionFeeCalculator(ABC):
    
    @abstractmethod
    def calculate_transaction_fee() -> float:
        pass

class AbstractFactory(ABC):
    
    @abstractmethod
    def create() -> object:
        pass

