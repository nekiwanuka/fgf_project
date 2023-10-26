from api.models import Transaction
import datetime
from django.utils.timezone import utc

from core.utilities.rest_exceptions import (ValidationError)
from business_logic.payments.verify_transaction import verify_ug_mobilemoney_charge


def delete_uninitiated_transactions():
    print('\nJob: deleting uninitiated transactions...')
    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    transactions = Transaction.objects.filter(status='Pending Initiation')

    for transaction in transactions:
        if(((now - transaction.created_at).total_seconds())/60 > 1800): # 1800
            pass
            #transaction.delete()
            #transaction.save

def change_transaction_status():
    pass
    # transactions = Transaction.objects.filter(status='Pending Initiation')
    # for transaction in transactions:
    #     transaction_reference_id = transaction.transaction_id
    #     if not verify_ug_mobilemoney_charge(transaction_reference_id):
    #         continue
    #         # raise ValidationError({'transaction_reference_id': 'Invalid transaction_reference_id. The system could not verify transaction made with this transaction_reference_id'})
    #     print('\nJob: Changing Transaction status from "Pending Initiation" to "Pending Approval"')
    #     transaction_details = verify_ug_mobilemoney_charge(transaction_reference_id)

    #     if transaction_details:            
    #         transaction.status = 'Pending Approval'
    #         transaction.save()
    #         # print(transaction_details)
    #         status = transaction_details['status']
    #         if status == 'successful':
    #             transaction.status = 'Successful'
    #             transaction.save()
