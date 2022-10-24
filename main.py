# modules
import requests
import json

# config files
from config import USER_KEY, APP_TOKEN

def get_joke():
    headers = {"Accept": "application/json"}
    request = requests.get(url="https://icanhazdadjoke.com/", headers=headers)
    request = json.loads(request.text)
    return request

def send_joke(joke, request):
    try:
        r = requests.post("https://api.pushover.net/1/messages.json", data=joke)
        print("Joke Sent")
        print(r.text)
    except Exception as e:
        print(f"Something went wrong!, {e}: {request['status']}")

request = get_joke()

# Joke
joke = {
    "token": APP_TOKEN,
    "user": USER_KEY,
    "message": request['joke']
}

send_joke(joke, request)


