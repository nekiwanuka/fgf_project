"""
2. Payments and Charges
    2.3. Medihub (Per Product, Vendor Incurs)
        - Markup fee (MF)
        For each of the Product in the Order,
            - Remaining Fee = Remaining Fee + (Product Gross Selling Price (PGSP) - Markup fee (MF))


Medihub Sales and Payments Oriented User Stories
    As a Medihub, I want to;
    - View Account balance
        - 1. Medihub Main Account
        - 2. Medihub Vendors Account
        - 3. Medihub Business Account
        - 4. Medihub Couriers Account
    - Deduct a markup fee from each product sold through the system.
    - Aggregate all the markup fees from all the products of an order.
    - Initiate and effect transaction (Credit Medihub Account with Markup fees of a certain order).
        - Debit : Medihub Main Account
        - Credit: Medihub Business Account
    - View markup fee transactions made.
    - Effect payments of confirmed sales (Medihub to Vendor)
        - Debit : Medihub Vendors Account
        - Credit: Specific Vendor Account
    - Effect payments of confirmed deliveries (Medihub to Courier)
        - Debit : Medihub Couriers Account
        - Credit: Specific Vendor Account


"""