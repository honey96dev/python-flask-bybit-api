import bybit_api

if __name__ == "__main__":
    print('order_create\t', bybit_api.order_create(side='Buy', symbol='BTCUSD', order_type='Market', qty=10, price=5000,
                                                   time_in_force='GoodTilCancel'))
    print('order_list\t', bybit_api.order_list(symbol='BTCUSD'))
    print('order_cancel\t', bybit_api.order_cancel('886b0b8d-ff1d-4e1a-a1cc-9900ac213d11'))
    print('stop_order_create\t', bybit_api.stop_order_create(side='Buy', symbol='BTCUSD', order_type='Market',
                                                             qty=100, price=110, base_price=300, stop_px=100,
                                                             time_in_force='GoodTillCancel'))
    print('stop_order_list\t', bybit_api.stop_order_list())
    print('stop_order_cancel\t', bybit_api.stop_order_cancel('7ef78b68-e879-4eea-bade-d2fc8f96682b'))
    print('user_leverage\t', bybit_api.user_leverage())
    print('user_leverage_save\t', bybit_api.user_leverage_save(10, 'EOSUSD'))
    print('position_list\t', bybit_api.position_list())
    print('position_change\t', bybit_api.position_change(0.2, 'BTCUSD'))
    print('last_funding_rate\t', bybit_api.last_funding_rate('BTCUSD'))
    print('last_funding_fee\t', bybit_api.last_funding_fee('BTCUSD'))
    print('predicted_funding_rate_fee\t', bybit_api.predicted_funding_rate_fee('BTCUSD'))
    print('trade_records\t', bybit_api.trade_records('739a5dde-c531-4de5-955a-d38f2fd4ccd9'))
