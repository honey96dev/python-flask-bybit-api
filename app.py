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


if __name__ == '__main__':
    context = ('domain.crt', 'domain.key')
    # app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
    app.run(port=443, ssl_context=context)
