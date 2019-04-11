import hashlib
import hmac
import base64

api_key = 'CtXGhVF2ubhX72V5aA'


def float_parser(x):
    res = 0
    try:
        res = float(x)
    except:
        res = 0

    return res


def int_parser(x):
    res = 0
    try:
        res = int(x)
    except:
        res = 0

    return res


def generate_hmac_sha256_hash(secret, message):
    message_bytes = bytes(message, 'utf-8')
    secret_bytes = bytes(secret, 'utf-8')

    return hmac.new(secret_bytes, message_bytes, hashlib.sha256)


def generate_hmac_sha256_hex(secret, message):
    hmac_hash = generate_hmac_sha256_hash(secret, message)
    return hmac_hash.hexdigest()


def generate_hmac_sha256_base64(secret, message):
    hmac_hash = generate_hmac_sha256_hash(secret, message)
    return base64.b64encode(hmac_hash.digest())


def generate_params_string(params):
    param_string = 'api_key={}'.format(api_key)
    for key, value in params.items():
        if (value is not None):
            param_string = '{}&{}={}'.format(param_string, key, value)

    return param_string
