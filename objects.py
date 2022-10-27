import requests
import json
from config import APP_TOKEN, USER_KEY

class Joke:
    def __init__(self):
        pass

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

    params = {
    "token": APP_TOKEN,
    "user": USER_KEY,
    "message": get_joke()['joke']
}
