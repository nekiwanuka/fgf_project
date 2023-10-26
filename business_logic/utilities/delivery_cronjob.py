from django.utils.timezone import utc
import datetime
from api.models import (Delivery, OrderReturn)


def change_delivery_status(request):
    deliveries = Delivery.objects.all().filter(payment_status='Frozen')
    orders = OrderReturn.objects.all()
    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    # seconds in a fortnight
    two_weeks = 1209600

    for delivery in deliveries:
        timediff = now - delivery.created_at

        for order in orders:
            if(delivery.order.id == order.order.id and timediff.total_seconds() > two_weeks):
                delivery.payment_status = 'Cancelled'
                delivery.save()

            else:
                delivery.payment_status = 'Due'
                delivery.save()
