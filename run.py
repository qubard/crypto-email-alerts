from uuid import uuid1
from datetime import datetime

from src import alert_loader, condition, binance, simple_mail

import schedule
import time

def sendMail(alert):
    to = alert['to']
    cond = alert['condition']
    if to and condition:
        satisfied = condition.eval(cond, lambda pair: api.price(pair))
        if satisfied:
            time = datetime.now()
            uuid = str(uuid1())[:5] # Generate a (hopefully) unique uuid
            status = simple_mail.SimpleEmailMessage(to). \
                setSubject("%s (#%s)" % (cond, uuid)). \
                sendMessage("Your condition happened!\n %s" % time)
            return status
    return False

def job():
    # Query the API
    api.fetch_ticker_pairs()

    # Send out e-mails for satisfied conditions
    new_alerts = [alert for alert in alerts if not sendMail(alert)]

    # re-write the modified alerts to disk
    if len(new_alerts) != len(alerts):
        alert_loader.write(new_alerts)

# Initialize the API
api = binance.API()

# Load alerts off disk
alerts = alert_loader.load()
        
# Schedule the job
schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)