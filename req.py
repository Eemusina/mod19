import json
import requests

status = 'available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})

print(res.status_code)

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {"id": 9223372036854775807, "category": {"id": 0, "name": "string"}, "name": "EVA0", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}], "status": "available"}
res = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, json=data)
print(res.status_code)
print(res.json())

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {"id": 9223372036854775807, "category": {"id": 0, "name": "string"}, "name": "EEEEE", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}], "status": "available"}
res = requests.put('https://petstore.swagger.io/v2/pet', json=data)
print(res.status_code)
print(res.json())

petid = "9223372036854775807"
headers = {'accept': 'application/json'}
res = requests.delete(f'https://petstore.swagger.io/v2/pet/{petid}', headers=headers)
print(res.status_code)
print(res.json())

