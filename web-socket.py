from global_constant import api_key, websocket_base_url, secret_key
from my_functions import eprint, get_current_timestamp, generate_hmac_sha256_hex, generate_params_string
import websocket
import json
import time


def ws_open():
    expires = get_current_timestamp()
    signature_param = 'GET/realtime{}'.format(expires)
    signature = generate_hmac_sha256_hex(secret_key, signature_param)
    params = {
        'api_key': api_key,
        'expires': expires,
        'signature': signature
    }
    params_string = generate_params_string(params)
    ws_query = '{}?{}'.format(websocket_base_url, params_string)
    # print(ws_query)
    ws = websocket.WebSocket()
    ws.connect(ws_query)
    # print('ws.connect', ws.connect(ws_query))
    return ws
    # ws.run_forever()
    # params = {
    #     'op': 'auth',
    #     'args': [api_key, expires, signature]
    # }
    # ws_query = json.dumps(params)
    # print(ws.send(ws_query))
    # ws.run_forever(sslopt={"check_hostname": False})


def ws_send_heartbeat():
    ws = ws_open()
    params = {
        'op': 'ping'
    }
    params_string = json.dumps(params)
    print('send', params_string)
    ws.send(params_string)
    ret_res = ws.recv()
    ws.close()
    return ret_res


def ws_order_book25(symbol):
    ws = ws_open()
    params = {
        'op': 'subscribe',
        'args': [
            'orderBook25.{}'.format(symbol)
        ]
    }
    params_string = json.dumps(params)
    print('send', params_string)
    ws.send(params_string)
    ret_res = ws.recv()
    ws.close()
    return ret_res


def ws_kline(symbol = '*', interval = '*'):
    ws = ws_open()
    params = {
        'op': 'subscribe',
        'args': [
            'kline.{}.{}'.format(symbol, interval)
        ]
    }
    params_string = json.dumps(params)
    print('send', params_string)
    ws.send(params_string)
    ret_res = ws.recv()
    ws.close()
    return ret_res


symbols = ['*', 'BTCUSD', 'ETHUSD']
kline_intervals = ['*','1m', '3m', '5m', '15m', '30m',
                         '1h', '2h', '3h', '4h', '6h',
                         '1d', '3d',
                         '1w', '2w',
                         '1M']

eprint('#ws_send_heartbeat', ws_send_heartbeat())
time.sleep(0.5)

for symbol in symbols:
    eprint('#ws_order_book25({})'.format(symbol), ws_order_book25(symbol))
time.sleep(0.5)


# eprint('#ws_kline({}, {})'.format('*', '*'), ws_kline())
# for symbol in symbols:
#     eprint('#ws_kline({}, {})'.format(symbol, '*'), ws_kline(symbol))
# for interval in kline_intervals:
#     eprint('#ws_kline({}, {})'.format('*', interval), ws_kline(interval=interval))
for symbol in symbols:
    for interval in kline_intervals:
        eprint('#ws_kline({}, {})'.format(symbol, interval), ws_kline(symbol, interval))
time.sleep(0.5)

