"""

Generic Flow of the Payments through the Medihub Platform.
1. Setting Prices
    1.1.
        Vendor
        - Set price for a product in stock. ==> Product Gross Selling Price (PGSP).
            Product Gross Selling Price (PGSP) = Product Net Selling Price (PNSP) + Markup

2. Payments and Charges

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


"""