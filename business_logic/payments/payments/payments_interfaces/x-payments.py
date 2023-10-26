"""
Proposed Finance Accounts
    - 1. Medihub Main Account
        - 2. Medihub Vendors Account
        - 3. Medihub Business Account
        - 4. Medihub Couriers Account

Possible Transaction Types
    1. Transfer
    2. Withdraw
    3. Deposit

Generic Flow of the Payments through the Medihub Platform.
1. Setting Prices
    1.1.
        Vendor
        - Set price for a product in stock. ==> Product Gross Selling Price (PGSP).
            Product Gross Selling Price (PGSP) = Product Net Selling Price (PNSP) + Markup

2. Payments and Charges
    2.1. Client (Per Order)
        - Gross Payment for Order (GPO)
        - Remaining Fee = Gross Payment for Order (GPO)

    2.2. Payments Service Provider (Per Order, Client Incurs)
        - Payments Service Fee (PSF)
        - Remaining Fee = Gross Payment for Order (GPO) - Payments Service Fee (PSF)

    2.4. Courier (Per Product, Client Incurs)
        - Product Delivery fee (PDF)
        For each of the Product in the Order,
            - Remaining Fee = Remaining Fee + (Product Gross Selling Price (PGSP) - Product Delivery fee (PDF))

    2.3. Medihub (Per Product, Vendor Incurs)
        - Markup fee (MF)
        For each of the Product in the Order,
            - Remaining Fee = Remaining Fee + (Product Gross Selling Price (PGSP) - Markup fee (MF))

    2.5. Vendor (Per Product)
        For each of the Product in Stock,
            - Product Net Selling Price (PNSP) = Product Gross Selling Price (PGSP) - Markup fee (MF)


Vendor Sales and Payments Oriented User Stories
    As a vendor, I want to;
    - Set price for a product in stock. ==> Product Gross Selling Price (PGSP).
        Product Gross Selling Price (PGSP) = Product Net Selling Price (PNSP) + Markup
    - Determine the Product Net Selling Price (PNSP) for a product in stock.
        Product Net Selling Price (PNSP) = Product Gross Selling Price (PGSP) - Markup
    - View order(s) palced against a product or list of products in stock.
    - View sales made for a product or list of products in stock.
        - Sales with in a space of less than 2 weeks (14 Days)
    - Bill for sales made:
        Initiate Transaction / Payment (Medihub to Vendor) for a Product or Products sold (Within a space of not less than two week / 14 Days)
    - View Transactions Pending Approval:
         Pending Transactions / Payments (Medihub to Vendor) for a Product or Products sold.
    - View Transactions Approved but Pending Payments:
         Pending Transactions / Payments (Medihub to Vendor) for a Product or Products sold.
    - View Paid off Transactions:

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

Payments Service Privider User Stories
    As a Payments gateway, I want to;
    - Receive payments transaction (out of our control as medihub developers)
    - Make transfer of payment from one account to the other
    - Avail transaction details to authenticated Users

Client Sales and Payments Oriented User Stories
    As a Client, I want to;
    - Brouse a list of products
    - Choose products of interest

    - Checkout Payments
    - Make Payments

"""