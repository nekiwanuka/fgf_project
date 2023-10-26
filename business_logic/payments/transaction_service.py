from rave_python import Rave, RaveExceptions, Misc
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

public_key = os.getenv('RAVE_PUBLIC_KEY')
secret_key = os.getenv('RAVE_SECRET_KEY')

rave = Rave(public_key, secret_key, usingEnv=True, production=True)


# rave = Rave(os.getenv('RAVE_PUBLIC_KEY'), os.getenv(
#     'RAVE_SECRET_KEY'))

card_payload = {
    "tx_ref": "MC-1585230950599",
    "cardno": "5438898014560229",
    "cvv": "828",
    "expirymonth": "09",
    "expiryyear": "21",
    "amount": "1500",
    "IP": "355426087298442",
    "email": "user@flw.com",
    "phonenumber": "0777127289",
    "currency": "UGX",
    "firstname": "Timothy",
    "lastname": "masiko",
}

def get_payment_details(response):
    _response = response
    print(type(_response)=='dict')
    payment_details = {}
    print(type(payment_details)=='dict')
    for key, value in _response.items():
        payment_details[key] = value
    return (payment_details)


def makeCardCharge(payload):
    try:
        res = rave.Card.charge(payload)

        if res["suggestedAuth"]:
            arg = Misc.getTypeOfArgsRequired(res["suggestedAuth"])

            if arg == "pin":
                Misc.updatePayload(res["suggestedAuth"], payload, pin="3310")
            if arg == "address":
                Misc.updatePayload(res["suggestedAuth"], payload, address={
                                   "billingzip": "07205", "billingcity": "Hillside", "billingaddress": "470 Mundet PI", "billingstate": "NJ", "billingcountry": "US"})

            res = rave.Card.charge(payload)

        if res["validationRequired"]:
            rave.Card.validate(res["flwRef"], "")

        res = rave.Card.verify(res["txRef"])
        print(res["transactionComplete"])

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



# verify_ug_mobilemoney_charge('MC-1625224413310')
# makeCardCharge(card_payload)
