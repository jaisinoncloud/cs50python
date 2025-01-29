#modules
  
import random
import statistics
import sys
import os
import cowsay
import requests
import json
import mymodule

"""
choice = random.choice(["heads","tails"])
print(choice)

num = random.randint(1,10)
print(num)

cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)

print(statistics.mean([100,90]))

print(f"{sys.argv[0]} is executed by {sys.argv[1]}")
"""
"""
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print(f"Name is {sys.argv[1]}")
print(sys.path)
print(sys.version)
print(sys.executable)
print(os.__file__)

cowsay.trex("Hello Jai")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=weezer")
print(type(response))
#print(response.json())
#print(response.json()['results'][0]['trackName'])
#print(json.dumps(response.json()))
for result in response.json()['results']:
    print(result['trackName'])
"""
mymodule.hello("Jai")
print(__name__)