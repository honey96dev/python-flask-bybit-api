from flask import Flask
import hashlib
import hmac
import base64

app = Flask(__name__)

testnet_url = 'https://api-testnet.bybit.com/open-api'
mainnet_url = 'https://api.bybit.com/open-api'


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


@app.route('/order/list')
def order_list():
    
    secret = 't7T0YlFnYXk0Fx3JswQsDrViLg1Gh3DUU5Mr'
    message = 'api_key=B2Rou0PLPpGqcU0Vu2&leverage=100&symbol=BTCUSD&timestamp=1542434791000'
    print(generate_hmac_sha256_hex(secret, message))
    return generate_hmac_sha256_hex(secret, message)


if __name__ == '__main__':
    context = ('domain.crt', 'domain.key')
    # app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
    app.run(port=443, ssl_context=context)
