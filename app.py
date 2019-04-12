from flask import Flask

import rest_api

app = Flask(__name__)


@app.route('/order/create', methods=['POST'])
def order_create():
    return rest_api.order_create()


@app.route('/order/list', methods=['GET'])
def order_list():
    return rest_api.order_list()


@app.route('/order/cancel', methods=['POST'])
def order_cancel():
    return rest_api.order_cancel()


@app.route('/stop-order/create', methods=['POST'])
def stop_order_create():
    return rest_api.stop_order_create()


@app.route('/stop-order/list', methods=['GET'])
def stop_order_list():
    return rest_api.stop_order_list()


@app.route('/stop-order/cancel', methods=['POST'])
def stop_order_cancel():
    return rest_api.stop_order_cancel()


@app.route('/user/leverage', methods=['GET'])
def user_leverage():
    return rest_api.user_leverage()


@app.route('/user/leverage/save', methods=['POST'])
def user_leverage_save():
    return rest_api.user_leverage_save()


@app.route('/position/list', methods=['GET'])
def position_list():
    return rest_api.position_list()


@app.route('/position/change', methods=['POST'])
def position_change():
    return rest_api.position_change()


@app.route('/last-funding-fee', methods=['GET'])
def last_funding_fee():
    return rest_api.last_funding_fee()


@app.route('/predicted-funding-rate-fee', methods=['GET'])
def predicted_funding_rate_fee():
    return rest_api.predicted_funding_rate_fee()


@app.route('/trade-records', methods=['GET'])
def trade_records():
    return rest_api.trade_records()


if __name__ == '__main__':
    context = ('domain.crt', 'domain.key')
    # app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
    app.run(port=443, ssl_context=context)
