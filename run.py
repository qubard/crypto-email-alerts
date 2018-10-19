from uuid import uuid1
from datetime import datetime

from src import alert_loader, condition, binance, simple_mail

# Load alerts off disk
alerts = alert_loader.load()

# Query the API
api = binance.API()
api.fetch_ticker_pairs()

# Send out e-mails for satisfied conditions
for alert in alerts:
    to = alert['to']
    cond = alert['condition']
    if to and condition:
        satisfied = condition.eval(cond, lambda pair: api.price(pair))
        if satisfied:
            time = datetime.now()
            uuid = str(uuid1())[:5] # Generate a (hopefully) unique uuid
            status = simple_mail.SimpleEmailMessage(to).setSubject("%s (#%s)" % (cond, uuid)).sendMessage("Your condition happened!\n %s" % time)
            print("Sent an e-mail to %s, Status: %s" % (to, status))

