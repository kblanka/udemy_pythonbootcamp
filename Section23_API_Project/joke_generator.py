import requests
import pyfiglet
from random import choice
from colorama import init
from termcolor import colored

init()

def print_art(msg, color):
  ascii_art = pyfiglet.figlet_format(msg)
  print(colored(ascii_art, color))
  
welcome_msg = "Joke Generator"  
print_art(welcome_msg, "cyan")

url = "https://icanhazdadjoke.com/search"
user_topic = input("Let me tell you a joke! Please give me a topic: ")

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": user_topic}
).json()

num_of_jokes = (response["total_jokes"])
results = response["results"]

if num_of_jokes > 1:
  print(
    f"I've got {num_of_jokes} jokes about {user_topic}. Here is one:\n",
    choice(results)["joke"]
  )
elif num_of_jokes == 1:
  print(
    f"I've got one joke about {term}. Here it is:\n",
    results[0]["joke"]
  )
elif num_of_jokes == 0:
  print(f"Sorry, we can't find a joke about {user_topic}.")

