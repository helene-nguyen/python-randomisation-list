# global variable
x = 'amazing'

def amazing_func():
    print(f"The world is {x} !")
    
amazing_func()

# global and local variables with same name
my_var = 'awesome'

def awesome_func():
    # local variable
    my_var = 'REALLY awesome'
    print(f"The world is {my_var}")

awesome_func()

print(f"The other world is {my_var} !")

# create a global inside a function
def global_func():
    global the_var
    the_var = 'Coraline'
    
global_func()

print(f"It's {the_var} ! Not Caroline at all.")