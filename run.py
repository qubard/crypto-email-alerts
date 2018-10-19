from uuid import uuid1
from datetime import datetime

from src import alert_loader, condition, binance, simple_mail

import schedule
import time

def getSatisfiedConditions(conditions):
    return list(filter(lambda cond: condition.eval(cond, lambda pair: api.price(pair)), conditions))

# Set difference seems unnecessary here
def getUnsatisfiedConditions(conditions):
    return list(filter(lambda cond: not condition.eval(cond, lambda pair: api.price(pair)), conditions))
    
def validAlert(alert):
    return alert['to'] and alert['conditions']
    
"""
Send an e-mail for alert's valid conditions.
returns true if mail was attempted to be sent
"""
def sendMail(alert):
    if validAlert(alert):
        # Only consider conditions which are satisfied
        to = alert['to']
        conditions = getSatisfiedConditions(alert['conditions'])
        for cond in conditions:
            time = datetime.now()
            uuid = str(uuid1())[:5] # Generate a (hopefully) unique uuid
            status = simple_mail.SimpleEmailMessage(to). \
                setSubject("%s (#%s)" % (cond, uuid)). \
                sendMessage("Your condition happened!\n %s" % time)
        return len(conditions) > 0
    return False

def job():
    global alerts
    global api
    
    modified = False
    
    # Query the API
    api.fetch_ticker_pairs()

    # Send out e-mails for satisfied conditions and keep unsatisfied conditions in the list
    for alert in alerts:
        if sendMail(alert):
            unsatisfiedConditions = getUnsatisfiedConditions(alert['conditions'])
            alert['conditions'] = unsatisfiedConditions
            modified = True
    
    if modified:
        # Get rid of any alerts with no conditions
        alerts = [alert for alert in alerts if len(alert['conditions']) > 0]
        # Re-write the modified alerts to disk
        alert_loader.write(alerts)
        
# Initialize the API
api = binance.API()

# Load alerts off disk
alerts = alert_loader.load()
        
# Schedule the job
schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)