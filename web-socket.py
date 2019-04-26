import json

import websocket

import global_constant
import my_functions


# def ws_open():
#     ws_query = '{}'.format(websocket_base_url)
#     ws = websocket.WebSocket()
#     ws.connect(ws_query)
#     return ws
#
#
# def ws_send_heartbeat():
#     ws = ws_open()
#     params = {
#         'op': 'ping'
#     }
#     params_string = json.dumps(params)
#     ws.send(params_string)
#     ret_res = ws.recv()
#     ws.close()
#     return ret_res
#
#
# def ws_order_book25(symbol):
#     ws = ws_open()
#     params = {
#         'op': 'subscribe',
#         'args': [
#             'orderBook25.{}'.format(symbol)
#         ]
#     }
#     params_string = json.dumps(params)
#     ws.send(params_string)
#     ret_res = ws.recv()
#     ws.close()
#     return ret_res
#
#
# def ws_kline(symbol='*', interval='*'):
#     ws = ws_open()
#     params = {
#         'op': 'subscribe',
#         'args': [
#             'kline.{}.{}'.format(symbol, interval)
#         ]
#     }
#     params_string = json.dumps(params)
#     print('send', params_string)
#     ws.send(params_string)
#     ret_res = ws.recv()
#     ws.close()
#     return ret_res


def on_ws_message(ws, message):
    my_functions.eprint('message', message)


def on_ws_error(ws, error):
    my_functions.eprint('error', error)


def on_ws_close(ws):
    my_functions.eprint("### closed ###")


def on_ws_open(ws):
    my_functions.eprint("### opened ###")
    expires = my_functions.get_current_timestamp()
    signature_param = 'GET/realtime{}'.format(expires)
    signature = my_functions.generate_hmac_sha256_hex(global_constant.secret_key, signature_param)
    params = {
        'op': 'auth',
        'args': [global_constant.api_key, expires, signature]
    }
    ws_query = json.dumps(params)
    ws.send(ws_query)
    # ws.send('{"op":"subscribe","args":["position"]}')
    ws.send('{"op": "subscribe", "args": ["orderBook25.BTCUSD"]}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(global_constant.websocket_base_url,
                                on_message=on_ws_message,
                                on_error=on_ws_error,
                                on_close=on_ws_close)

    ws.on_open = on_ws_open
    ws.run_forever()

