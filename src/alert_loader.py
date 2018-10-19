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

def write(data):
    new_dict = {}
    new_dict['alerts'] = data
    with open(config.alerts_dir, 'w') as f:
        json.dump(new_dict, f, indent=4)