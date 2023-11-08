import random

print(random.random()) # numbers between 0 and 1 but 1 is exculded

x = random.randrange(0, 10)
print(f"The random value is: {x}")

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

# Create a random decimal number between 0 and 5
random_decimal = random_float * random_integer
print(random_decimal)