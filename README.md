# Python journey

![banner](./__docs__/media/banner.png)

## Introduction

For this session, we'll learn control randomisation.

## Summary

- [Requirements](#requirements)
- [Tools and version](#tools-and-versions)
- [Projects](#project)
  - Randomisation
  - Heads or tails
  - Nested list
- [What you'll learn](#what-youll-learn)

- Useful resources :

  - [Sources](#sources)

## Requirements

Python installed and an IDE or online editor like: <https://replit.com/>

## Tools and versions

- OS

  - Linux OS -
  - Windows OS -

- IDE

  - VSCodium v1.81.1

- Techno
  - Python v3.11.4

## Project

### Randomisation

Import the module

```py
import random

# numbers between 0 and 1 but 1 is exculded
print(random.random())

x = random.randrange(0, 10)
print(f"The random value is: {x}")
```

### Heads or Tails

```py
import random

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
```

### Nested list

```py
fruits = ["strawberry", "apple", "orange"]
vegetables = ["spinach", "tomato", "kale"]

nested_list = [fruits, vegetables]
```

## Some tips

Functions and global variables

- Global variables

```py
# global variable
x = 'amazing'

def amazing_func():
    print(f"The world is {x} !")

amazing_func() #Expected outout The world is amazing
```

- Global variables and function local variable

```py
# global and local variables with same name
my_var = 'awesome'

def awesome_func():
    # local variable
    my_var = 'REALLY awesome'
    print(f"The world is {my_var}")

awesome_func() # The world is REALLY awesome

print(f"The other world is {my_var} !") # The other world is awesome
```

- Define a global variable inside a function

```py
def global_func():
    global the_var
    the_var = 'Coraline'

global_func() #call the function for using the global variable

print(f"It's {the_var} ! Not Caroline at all.") # Output: It's Coraline ! Not Caroline at all.
```

Create a module

- Create a main file called main.py
- Create another file called new_module
- Inside new_module, create a variable or function
- To use your new module, just import the file name

new_module.py

```py
pi = 3.14159246

def say_hello():
    print("Oh hello!")
```

main.py

```py
import new_module

print(new_module.pi)
# Say hello form new module
new_module.say_hello()
```

## What you'll learn

Create a module, working with nested list, create functions and scope of variables.

---

## Sources

- [Random Module](https://www.w3schools.com/python/module_random.asp)
