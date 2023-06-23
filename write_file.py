# writing to json file
import json

a = 'res.json'

with open(a, 'w') as f:
    json.dump(res, f)