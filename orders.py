from flask import request
import requests
import json
from global_constant import server_base_url, api_key, secret_key
from my_functions import generate_hmac_sha256_hex, generate_params_string, get_current_timestamp


def order_create():
    params = request.args
    order_link_id = params.get('order_link_id')
    order_type = params.get('order_type')
    price = params.get('price')
    qty = params.get('qty')
    side = params.get('side')
    symbol = params.get('symbol')
    time_in_force = params.get('time_in_force')
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


def order_list():
    params = request.args
    order_id = params.get('order_id')
    order_link_id = params.get('order_link_id')
    symbol = params.get('symbol')
    sort = params.get('sort')
    order = params.get('order')
    page = params.get('page')
    limit = params.get('limit')
    order_status = params.get('order_status')
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
