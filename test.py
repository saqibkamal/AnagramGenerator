import requests
BASE_URL = "http://127.0.0.1:233" 

test = {"text": 'HelloWorld'}

response = requests.post("{}/process".format(BASE_URL), json = test)

print(response.json())