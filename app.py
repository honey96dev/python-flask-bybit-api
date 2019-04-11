from flask import Flask, request
import requests
import json
from my_functions import int_parser, float_parser, generate_hmac_sha256_hex

app = Flask(__name__)

###### https://api.bybit.com/v2/private/execution/list


testnet_url = 'https://api-testnet.bybit.com'
mainnet_url = 'https://api.bybit.com'
# api_key = 'B2Rou0PLPpGqcU0Vu2'
# secret_key = 't7T0YlFnYXk0Fx3JswQsDrViLg1Gh3DUU5Mr'
api_key = '7270jBNmOvsunjeGL5'
secret_key = 'uXvIZ3WuZFu1opxhfY8WGqap5eMJY9aDpzey'
server_base_url = mainnet_url


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

    url = '{}/GET/realtime'.format(server_base_url)
    # timestamp = calendar.timegm(time.gmtime()) + 1000
    try:
        r = requests.get(url=url)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)
        timestamp = int_parser(float_parser(rows['time_now']) * 1000)

        print("timestamp", timestamp)
    except:
        return 'error'

    params_string = 'api_key={}&timestamp={}'
    params_string = params_string.format(api_key, timestamp)
    # params_string = 'api_key={}&limit={}&order={}&order_id={}&order_link_id={}&' + \
    #                 'order_status={}&page={}&sort={}&symbol={}&timestamp={}'
    # params_string = params_string.format(api_key, limit, order, order_id, order_link_id,
    #                                      order_status, page, sort, symbol, timestamp)
    sign = generate_hmac_sha256_hex(secret_key, params_string)


    url = '{}/open-api/order/list'.format(server_base_url)

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
        'timestamp': timestamp,
        'sign': sign,
    }

    try:
        r = requests.get(url=url, params=params)

        formatted_string = r.text.replace("'", '"')
        rows = json.loads(formatted_string)

        return json.dumps(rows)
    except:
        return 'error'

    # secret = 't7T0YlFnYXk0Fx3JswQsDrViLg1Gh3DUU5Mr'
    # message = 'api_key=B2Rou0PLPpGqcU0Vu2&leverage=100&symbol=BTCUSD&timestamp=1542434791000'
    # return generate_hmac_sha256_hex(secret, message)



if __name__ == '__main__':
    context = ('domain.crt', 'domain.key')
    # app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
    app.run(port=443, ssl_context=context)


# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
#     try:
#         print(order_list())
#     except:
#         time.sleep(5)
#     # do your stuff
#     s.enter(1, 1, do_something, (sc,))
#
# s.enter(1, 1, do_something, (s,))
# s.run()
