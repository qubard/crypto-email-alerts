import json
import config

def load():
    data = {}
    with open(config.alerts_dir) as f:
        data = json.load(f)

    alerts = data['alerts']
    
    if not alerts:
        return None
        
    return alerts
