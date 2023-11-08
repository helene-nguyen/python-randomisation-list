# Write a progam that will select a random name from a list of names
from constants import names_string
import random

names = names_string.split(', ')
random_value = random.randint(0, len(names)-1)

random_name = names[random_value]

print(f'{random_name} is going to buy the meal today!')
