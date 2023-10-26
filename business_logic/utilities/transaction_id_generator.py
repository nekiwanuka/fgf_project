import random
import string

def get_transaction_id():
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(16))
    ref = "MH-"+result_str
    return ref
