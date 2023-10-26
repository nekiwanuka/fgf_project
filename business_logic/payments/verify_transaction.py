from rave_python import Rave, RaveExceptions, Misc
import os
from dotenv import load_dotenv
import asyncio

load_dotenv(verbose=True)

public_key = os.getenv('RAVE_PUBLIC_KEY')
secret_key = os.getenv('RAVE_SECRET_KEY')

rave = Rave(publicKey = public_key, secretKey = secret_key, production=True, usingEnv=True)

def get_payment_details(response):
    _response = response
    payment_details = {}
    for key, value in _response.items():
        payment_details[key] = value
    return (payment_details)


def verify_cardcharge(transaction_id):
    try:
        _transaction_id = transaction_id
        response = rave.Card.verify(_transaction_id)
        return get_payment_details(response)

    except RaveExceptions.CardChargeError as e:
        print(e.err["errMsg"])
        print(e.err["flwRef"])

    except RaveExceptions.TransactionValidationError as e:
        print(e.err)
        print(e.err["flwRef"])

    except RaveExceptions.TransactionVerificationError as e:
        print(e.err["errMsg"])
        print(e.err["txRef"])


async def _verify_ug_mobilemoney_charge(transaction_id):

    try:
        res = rave.UGMobile.verify(txRef=transaction_id)
        return res
        # return (res["transactionComplete"])

    except RaveExceptions.TransactionChargeError as e:
        raise e
        # return ("Transaction Charge error")

    except RaveExceptions.TransactionVerificationError as e:
        # raise e
        return ('Transaction Verification Error')


async def verify_ug_mobilemoney_charge(transaction_id):
    _response = await _verify_ug_mobilemoney_charge(transaction_id)
    # response = get_payment_details(_response)
    return _response
