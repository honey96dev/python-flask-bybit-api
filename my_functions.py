from __future__ import print_function

import base64
import calendar
import hashlib
import hmac
import json
import sys
import time

import requests

from global_constant import server_base_url, api_key


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


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


def get_current_timestamp():
    timestamp = int_parser(calendar.timegm(time.gmtime()) * 1000) + 1000
    url = '{}/GET/realtime'.format(server_base_url)
    try:
        r = requests.get(url=url)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)
        timestamp = int_parser(float_parser(rows['time_now']) * 1000) + 1000
    finally:
        return timestamp
