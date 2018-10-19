from src import alert_loader, condition, binance

alerts = alert_loader.load()
print(alerts)

api = binance.API()
api.fetch_ticker_pairs()

for alert in alerts:
    print(alert, condition.eval(alert['condition'], lambda pair: api.price(pair)))
