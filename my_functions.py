
import hashlib
import hmac
import base64


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
    hash = generate_hmac_sha256_hash(secret, message)
    return hash.hexdigest()


def generate_hmac_sha256_base64(secret, message):
    hash = generate_hmac_sha256_hash(secret, message)
    return base64.b64encode(hash.digest())

def generate_param_string(params):
    a = 1
