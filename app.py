from flask import Flask, request
import hashlib
import hmac
import base64
import requests
import json

app = Flask(__name__)

testnet_url = 'https://api-testnet.bybit.com/open-api'
mainnet_url = 'https://api.bybit.com/open-api'
# api_key = 'B2Rou0PLPpGqcU0Vu2'
# secret_key = 't7T0YlFnYXk0Fx3JswQsDrViLg1Gh3DUU5Mr'
api_key = 'ndy9IwVo9jas6sTC29'
secret_key = 'KLFEIhm5j3DJu5hQgdiCNpNA3N60yVu39UP3'
server_base_url = testnet_url

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


@app.route('/order/list', methods=['GET'])
def order_list():
    params = request.args
    order_id = params.get('order_id', '')
    order_link_id = params.get('order_link_id', '')
    symbol = params.get('symbol', '')
    sort = params.get('sort', '')
    order = params.get('order', '')
    page = params.get('page', '')
    limit = params.get('limit', '')
    order_status = params.get('order_status', '')

    params_string = 'api_key={}'
    params_string = params_string.format(api_key)
    params_string = 'api_key={}&limit={}&order={}&order_id={}&order_link_id={}&' + \
                    'order_status={}&page={}&sort={}&symbol={}'
    params_string = params_string.format(api_key, limit, order, order_id, order_link_id,
                                         order_status, page, sort, symbol)
    sign = generate_hmac_sha256_hex(secret_key, params_string)


    url = '{}/order/list'.format(server_base_url)

    bybit_url = '{}/order/list?{}&sign={}'.format(server_base_url, params_string, sign)
    print(bybit_url)

    print(url)
    # defining a params dict for the parameters to be sent to the API
    params = {
        'api_key': api_key,
        'limit': limit,
        'order': order,
        'order_id': order_id,
        'order_link_id': order_link_id,
        'order_status': order_status,
        'page': page,
        'sort': sort,
        'symbol': symbol,
        'sign': sign,
    }

    r = requests.get(url=url, params=params)

    try:
        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return 'error'

    secret = 't7T0YlFnYXk0Fx3JswQsDrViLg1Gh3DUU5Mr'
    message = 'api_key=B2Rou0PLPpGqcU0Vu2&leverage=100&symbol=BTCUSD&timestamp=1542434791000'
    return generate_hmac_sha256_hex(secret, message)


if __name__ == '__main__':
    context = ('domain.crt', 'domain.key')
    # app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
    app.run(port=443, ssl_context=context)
