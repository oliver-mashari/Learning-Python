# Basic example 
"""
def say_hello():
    print("hello")
say_hello()
"""

# Basic example with arguments
"""
def say_hello(name):    
    print(f"Hello {name}!")
say_hello("Oliver")     # This requires an argument
say_hello()     # This will return an error because no argument has been passed
"""

# Basic example with arguments and argument defaults
"""
def say_hello(name="Cloud"):    
    print(f"Hello {name}!")
say_hello("Oliver")     # This requires an argument
say_hello()     # Because a default is set this is acceptable 
"""

# Basic example using return 
def add_numbers(num1, num2):
    return num1+num2
sum = add_numbers(10,20)
print(sum)