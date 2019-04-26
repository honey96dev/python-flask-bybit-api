import json

from flask import Flask, request

import bybit_api

app = Flask(__name__)


@app.route('/order/create', methods=['POST'])
def order_create():
    params = request.args
    order_link_id = params.get('order_link_id')
    order_type = params.get('order_type')
    price = params.get('price')
    qty = params.get('qty')
    side = params.get('side')
    symbol = params.get('symbol')
    time_in_force = params.get('time_in_force')
    return json.dumps(bybit_api.order_create(order_link_id, order_type, price, qty, side, symbol, time_in_force))


@app.route('/order/list', methods=['GET'])
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
    return json.dumps(bybit_api.order_list(order_id, order_link_id, symbol, sort, order, page, limit, order_status))


@app.route('/order/cancel', methods=['POST'])
def order_cancel():
    params = request.args
    order_id = params.get('order_id')
    return json.dumps(bybit_api.order_cancel(order_id))


@app.route('/stop-order/create', methods=['POST'])
def stop_order_create():
    params = request.args
    base_price = params.get('base_price')
    order_link_id = params.get('order_link_id')
    order_type = params.get('order_type')
    price = params.get('price')
    qty = params.get('qty')
    side = params.get('side')
    symbol = params.get('symbol')
    stop_px = params.get('stop_px')
    time_in_force = params.get('time_in_force')
    return json.dumps(bybit_api.stop_order_create(base_price, order_link_id, order_type, price, qty, side, symbol, stop_px, time_in_force))


@app.route('/stop-order/list', methods=['GET'])
def stop_order_list():
    params = request.args
    limit = params.get('limit')
    order = params.get('order')
    order_link_id = params.get('order_link_id')
    page = params.get('page')
    sort = params.get('sort')
    stop_order_id = params.get('stop_order_id')
    symbol = params.get('symbol')
    return json.dumps(bybit_api.stop_order_list(limit, order, order_link_id, page, sort, stop_order_id, symbol))


@app.route('/stop-order/cancel', methods=['POST'])
def stop_order_cancel():
    params = request.args
    stop_order_id = params.get('stop_order_id')
    return json.dumps(bybit_api.stop_order_cancel(stop_order_id))


@app.route('/user/leverage', methods=['GET'])
def user_leverage():
    return json.dumps(bybit_api.user_leverage())


@app.route('/user/leverage/save', methods=['POST'])
def user_leverage_save():
    params = request.args
    leverage = params.get('leverage')
    symbol = params.get('symbol')
    return json.dumps(bybit_api.user_leverage_save(leverage, symbol))


@app.route('/position/list', methods=['GET'])
def position_list():
    return json.dumps(bybit_api.position_list())


@app.route('/position/change', methods=['POST'])
def position_change():
    params = request.args
    margin = params.get('margin')
    symbol = params.get('symbol')
    return json.dumps(bybit_api.position_change(margin, symbol))


@app.route('/last-funding-rate', methods=['GET'])
def last_funding_rate():
    params = request.args
    symbol = params.get('symbol')
    return json.dumps(bybit_api.last_funding_rate(symbol))


@app.route('/last-funding-fee', methods=['GET'])
def last_funding_fee():
    params = request.args
    symbol = params.get('symbol')
    return json.dumps(bybit_api.last_funding_fee(symbol))


@app.route('/predicted-funding-rate-fee', methods=['GET'])
def predicted_funding_rate_fee():
    params = request.args
    symbol = params.get('symbol')
    return json.dumps(bybit_api.predicted_funding_rate_fee(symbol))


@app.route('/trade-records', methods=['GET'])
def trade_records():
    params = request.args
    order_id = params.get('order_id')
    return json.dumps(bybit_api.trade_records(order_id))


if __name__ == '__main__':
    context = ('domain.crt', 'domain.key')
    # app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
    app.run(port=443, ssl_context=context)
