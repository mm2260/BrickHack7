import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "book/1")
print(response.json())


response = requests.get(BASE + "object/2")
print(response.json())
