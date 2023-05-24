import requests
import json
URL = "http://127.0.0.1:8000/create"
print('success')
data = {
 'name': 'Sonam',
 'roll': 101,
 'city': 'Ranchi'
}

json_data = json.dumps(data)
context = {'data': json_data}
r = requests.post(url=URL, json=context)

data = r.json()
print(data)