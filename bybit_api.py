import json

import requests

from global_constant import server_base_url, api_key, secret_key
from my_functions import generate_hmac_sha256_hex, generate_params_string, get_current_timestamp


def order_create(order_link_id=None, order_type=None, price=None, qty=None, side=None, symbol=None, time_in_force=None):
    timestamp = get_current_timestamp()

    params = {
        'order_link_id': order_link_id,
        'order_type': order_type,
        'price': price,
        'qty': qty,
        'side': side,
        'symbol': symbol,
        'time_in_force': time_in_force,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/open-api/order/create'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.post(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def order_list(order_id=None, order_link_id=None, symbol=None, sort=None, order=None, page=None, limit=None,
               order_status=None):
    timestamp = get_current_timestamp()

    params = {
        'limit': limit,
        'order': order,
        'order_id': order_id,
        'order_link_id': order_link_id,
        'order_status': order_status,
        'page': page,
        'sort': sort,
        'symbol': symbol,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/open-api/order/list'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.get(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def order_cancel(order_id=None):
    timestamp = get_current_timestamp()

    params = {
        'order_id': order_id,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/open-api/order/cancel'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.post(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def stop_order_create(base_price=None, order_link_id=None, order_type=None, price=None, qty=None, side=None,
                      symbol=None, stop_px=None, time_in_force=None):
    timestamp = get_current_timestamp()

    params = {
        'base_price': base_price,
        'order_link_id': order_link_id,
        'order_type': order_type,
        'price': price,
        'qty': qty,
        'side': side,
        'stop_px': stop_px,
        'symbol': symbol,
        'time_in_force': time_in_force,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/open-api/stop-order/create'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.post(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def stop_order_list(limit=None, order=None, order_link_id=None, page=None, sort=None, stop_order_id=None, symbol=None):
    timestamp = get_current_timestamp()

    params = {
        'limit': limit,
        'order': order,
        'order_link_id': order_link_id,
        'page': page,
        'sort': sort,
        'stop_order_id': stop_order_id,
        'symbol': symbol,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/open-api/stop-order/list'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.get(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def stop_order_cancel(stop_order_id=None):
    timestamp = get_current_timestamp()

    params = {
        'stop_order_id': stop_order_id,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/open-api/stop-order/cancel'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.post(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def user_leverage():
    timestamp = get_current_timestamp()

    params = {
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/user/leverage'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.get(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def user_leverage_save(leverage=None, symbol=None):
    timestamp = get_current_timestamp()

    params = {
        'leverage': leverage,
        'symbol': symbol,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/user/leverage/save'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.post(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def position_list():
    timestamp = get_current_timestamp()

    params = {
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/position/list'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.get(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def position_change(margin=None, symbol=None):
    timestamp = get_current_timestamp()

    params = {
        'margin': margin,
        'symbol': symbol,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/position/change-position-margin'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.post(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def last_funding_rate(symbol=None):
    timestamp = get_current_timestamp()

    params = {
        'symbol': symbol,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/open-api/funding/prev-funding-rate'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.get(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def last_funding_fee(symbol=None):
    timestamp = get_current_timestamp()

    params = {
        'symbol': symbol,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/open-api/funding/prev-funding'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.get(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def predicted_funding_rate_fee(symbol=None):
    timestamp = get_current_timestamp()

    params = {
        'symbol': symbol,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/open-api/funding/predicted-funding'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.get(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )


def trade_records(order_id=None):
    timestamp = get_current_timestamp()

    params = {
        'order_id': order_id,
        'timestamp': timestamp,
    }
    params_string = generate_params_string(params)
    sign = generate_hmac_sha256_hex(secret_key, params_string)

    url = '{}/v2/private/execution/list'.format(server_base_url)

    params['api_key'] = api_key
    params['sign'] = sign

    try:
        r = requests.get(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return json.dumps(
            {'ret_msg': 'error'}
        )
