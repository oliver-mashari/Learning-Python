# scope and nested statememnts

# this is a global variable
name = ' This is a global string'

def greet():
    # name here is considered an enclosing
    # function local 
    name = 'oliver' 
    def hello():
        # if name was defined as part of hello()
        # it would be considered a local variable 
        print(f"hello {name}")
    hello()
greet()

# How to change a global variable within a function 
x = 50 
def func():
    # global keyword grabs global variable
    global x
    print(f"function x is {x}")
    # Local reassignment
    x = 100
    print(f"I just locally changed x to {x}")
func()
print(x)