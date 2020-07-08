import requests
BASE_URL = "https://anagram-flask-api.herokuapp.com/" 

test = {"text": 'HelloWorld'}

response = requests.post("{}/process".format(BASE_URL), json = test)

print(response.json())