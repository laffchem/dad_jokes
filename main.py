from objects import Joke

# Creates joke class
joke = Joke
# Request the Joke
r = joke.get_joke()
# Send the Joke
joke.send_joke(joke.params, r)

