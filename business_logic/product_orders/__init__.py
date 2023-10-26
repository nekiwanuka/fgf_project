"""
Order
    product x from vendor x (size 10)
    product y from vendor y (size 5)
    product x from vendor x (size 10)
    product z from vendor z (size 5)
    product a from vendor a (size 10)
    product z from vendor z (size 5)   

    Total sum of products (100,000/=)
    Delivery fee / Shipping fee = DF =?
    payment service fee (0.3%) SF = ?

1. Conert to Kg

2. determine the total size in kg
    total_size = 0
    for product in products:
        product_size = convert_to_kg(product.size, measurement_unit)
        total_size = total_size + product_size

3. get_client_distance()
    return method_by_timotj()

4. get_delivery_fee()
    
order = {
    products = [
        {
            size:10
        },{},{}
    ]
}
"""
