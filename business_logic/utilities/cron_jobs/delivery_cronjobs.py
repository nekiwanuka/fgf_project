from api.models import (Delivery, OrderReturn, OSPU_Order,
                        OSPU_Return, OrganizationSale)


def confirm_delivery():
    print('\nJob: confirming delivery...')
    deliveries = Delivery.objects.all().filter(payment_status='Frozen')
    for delivery in deliveries:
        successful_delivery = True
        delivery_order = delivery.order
        order_returns = OrderReturn.objects.all().filter(order=delivery_order)

        if (order_returns.exists()):

            for order_return in order_returns:
                if(order_return.return_record.replacement_status == 'Pending Replacement'):
                    successful_delivery = False
                    break

        else:
            ospu_orders = OSPU_Order.objects.all().filter(order=delivery_order)

            for ospu_order in ospu_orders:
                ospu_returns = OSPU_Return.objects.all().filter(osp_unit=ospu_order.osp_unit)

                if (ospu_returns.exists()):

                    for ospu_return in ospu_returns:
                        if(ospu_return.return_record.replacement_status == 'Pending Replacement'):
                            successful_delivery = False
                else:

                    organization_sales = OrganizationSale.objects.all().filter(
                        ospu_order=ospu_order)
                    if (organization_sales.exists()):
                        organization_sale = organization_sales[0]
                        organization_sale.sale.payment_status = 'Pending Payment'
                        organization_sale.sale.save()
            if(successful_delivery):
                delivery.status = 'Pending Payment'
                delivery.save()

