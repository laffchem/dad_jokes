# config files
from config import USER_KEY, APP_TOKEN
from logic import get_joke, send_joke

request = get_joke()

print(type(request))

# Joke
joke = {
    "token": APP_TOKEN,
    "user": USER_KEY,
    "message": request['joke']
}

send_joke(joke, request)


