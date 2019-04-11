from flask import Flask, request
import requests
import json
from global_constant import server_base_url, api_key, secret_key
from my_functions import generate_hmac_sha256_hex, generate_params_string, get_current_timestamp
import orders

app = Flask(__name__)


@app.route('/order/create', methods=['POST'])
def order_create():
    return orders.order_create()


@app.route('/order/list', methods=['GET'])
def order_list():
    return orders.order_list()
    # params = request.args
    # order_id = params.get('order_id')
    # order_link_id = params.get('order_link_id')
    # symbol = params.get('symbol')
    # sort = params.get('sort')
    # order = params.get('order')
    # page = params.get('page')
    # limit = params.get('limit')
    # order_status = params.get('order_status')
    #
    # # url = '{}/GET/realtime'.format(server_base_url)
    # # # timestamp = calendar.timegm(time.gmtime()) + 1000
    # # try:
    # #     r = requests.get(url=url)
    # #
    # #     formatted_string = r.text.replace("'", '"')
    # #     rows = json.loads(formatted_string)
    # #     timestamp = int_parser(float_parser(rows['time_now']) * 1000)
    # # except:
    # #     return 'error'
    # timestamp = get_current_timestamp()
    #
    # params = {
    #     'limit': limit,
    #     'order': order,
    #     'order_id': order_id,
    #     'order_link_id': order_link_id,
    #     'order_status': order_status,
    #     'page': page,
    #     'sort': sort,
    #     'symbol': symbol,
    #     'timestamp': timestamp,
    # }
    # params_string = generate_params_string(params)
    # # print(params_string)
    # # params_string = 'api_key={}&timestamp={}'
    # # params_string = params_string.format(api_key, timestamp)
    # # print(params_string)
    # # params_string = 'api_key={}&limit={}&order={}&order_id={}&order_link_id={}&' + \
    # #                 'order_status={}&page={}&sort={}&symbol={}&timestamp={}'
    # # params_string = params_string.format(api_key, limit, order, order_id, order_link_id,
    # #                                      order_status, page, sort, symbol, timestamp)
    # sign = generate_hmac_sha256_hex(secret_key, params_string)
    #
    # url = '{}/open-api/order/list'.format(server_base_url)
    #
    # # params = {
    # #     'api_key': api_key,
    # #     'limit': limit,
    # #     'order': order,
    # #     'order_id': order_id,
    # #     'order_link_id': order_link_id,
    # #     'order_status': order_status,
    # #     'page': page,
    # #     'sort': sort,
    # #     'symbol': symbol,
    # #     'timestamp': timestamp,
    # #     'sign': sign,
    # # }
    # params['api_key'] = api_key
    # params['sign'] = sign
    #
    # try:
    #     r = requests.get(url=url, params=params)
    #
    #     formatted_string = r.text.replace("'", '"')
    #     rows = json.loads(formatted_string)
    #
    #     return json.dumps(rows)
    # except:
    #     return 'error'


if __name__ == '__main__':
    context = ('domain.crt', 'domain.key')
    # app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
    app.run(port=443, ssl_context=context)
