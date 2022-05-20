import requests

endpoint = "http://127.0.0.1:8000/api/product/"

get_response = requests.get(endpoint, json={"product_id": 123})

# print (get_response.headers)
print (get_response.json())
# print (get_response.text)