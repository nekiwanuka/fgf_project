"""
Payments and Charges
    2.1. Client (Per Order)
        - Gross Payment for Order (GPO)
        - Remaining Fee = Gross Payment for Order (GPO)

Client Sales and Payments Oriented User Stories
    As a Client, I want to;
    - Brouse a list of products
    - Choose products of interest

    - Checkout Payments
    - Make Payments
"""

from abc import ABC as AbstarctClass, abstractmethod

class ClientPaymentsInterface(AbstarctClass):
    pass