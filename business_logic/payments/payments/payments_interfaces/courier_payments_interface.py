"""
2. Payments and Charges
    2.4. Courier (Per Product, Client Incurs)
        - Product Delivery fee (PDF)
        For each of the Product in the Order,
            - Remaining Fee = Remaining Fee + (Product Gross Selling Price (PGSP) - Product Delivery fee (PDF))

Courier Sales and Payments Oriented User Stories
    As a Courier, I want to;
    - View all Orders
    - View Pending orders (with Delivery fees)
    - View In Transit Orders (with Delivery fees)
    - View Deliveries made (Delivered Orders)

    - View all Payments
    - View Pending Payments: Devivery fees per Delivered Order
    - Bill for Deliveries made:
        Initiate Transaction / Payment (Medihub to Courier) for an Order or Products delivered (Within a space of not less than a month)
    - View Transactions Pending Approval:
         Pending Transactions / Payments (Medihub to Courier) for an Order or Products delivered.
    - View Transactions Apprived but Pending Payments:
         Pending Transactions / Payments (Medihub to Courier) for an Order or Products delivered.
    - View Successfull Transactions / Paid off bills:

"""

from abc import ABC as AbstarctClass, abstractmethod

class CourierPaymentsInterface(AbstarctClass):
    
    @abstractmethod
    def get_transaction_charge_fee():
        pass

    @abstractmethod
    def get_transaction_charge_fee():
        pass
