import requests
import json

headers = {"Accept": "application/json"}
request = requests.get(url="https://icanhazdadjoke.com/", headers=headers)
request = json.loads(request.text)




# print(joke)

