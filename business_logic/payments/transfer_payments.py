from rave_python import Rave, RaveExceptions, Misc
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

public_key = os.getenv('RAVE_PUBLIC_KEY')
secret_key = os.getenv('RAVE_SECRET_KEY')

rave = Rave(public_key, secret_key, usingEnv=True)


# def create_subaccount():
#     try:
#         # res = rave.SubAccount.create({
#         #     "account_bank": "044",
#         #     "account_number": "0690000032",
#         #     "business_name": "Jake Stores",
#         #     "business_email": "jdhhd@services.com",
#         #     "business_contact": "Amy Parkers",
#         #     "business_contact_mobile": "09083772",
#         #     "business_mobile": "0188883882",
#         #     "split_type": "flat",
#         #     "country": "UG",
#         #     "split_value": 3000,
#         #     "meta": [{"metaname": "MarketplaceID", "metavalue": "ggs-920900"}]
#         # })
#         # res = rave.SubAccount.fetch('RS_0A6C260E1A70934DE6EF2F8CEE46BBB3')

#         # RS_C45C6B555D5B86A8BD0A86ADE31C07EE

#         res2 = rave.SubAccount.fetch('RS_C45C6B555D5B86A8BD0A86ADE31C07EE')
#         print(res2)

#     except RaveExceptions.IncompletePaymentDetailsError as e:
#         print(e)

#     except RaveExceptions.PlanStatusError as e:
#         print(e.err)

#     except RaveExceptions.ServerError as e:
#         print(e.err)


def make_transfer(amount):
    try:
        res = rave.Transfer.initiate({
            "account_bank": "044",
            "account_number": "0690000033",
            "amount": amount,
            "narration": "New transfer",
            "currency": "UGX",
            "beneficiary_name": "TIMOTGHY"
        })
        print(res)

    except RaveExceptions.IncompletePaymentDetailsError as e:
        print(e)
        print(e.err["flwRef"])


# create_subaccount()
make_transfer()
