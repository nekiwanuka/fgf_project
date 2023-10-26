from api.models import Delivery
import datetime
from django.utils.timezone import utc


def delivery_status_update():
    print('\nJob: updating delivery status')
    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    deliveries = Delivery.objects.filter(payment_status='Frozen')

    for delivery in deliveries:
        if(((now - delivery.created_at).total_seconds())/60 > 20160):
            delivery.payment_status = 'Pending Payment'
            delivery.save()
