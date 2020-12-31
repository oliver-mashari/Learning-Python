""" syntax of a while loop
while some_boolean_condition:
    # execute some code 
else:
    # execute some code
"""
x = 0 
# while x < 5:
#     # This will execute an infinite loop
#     print(f"current value: {x}")
while x < 5:
    print(f"current value: {x}")
    x = x + 1
    """ x +=    # more compact way of writting the above line"""
else:
    print("x is not less than 5")

# break, continue, pass
x = [1,2,3]
for number in x:
    pass    # doe nothing but for loops expect some sort of code this is useful for placeholders

my_string = "Oliver"
for letter in my_string:
    if letter == 'l':
        continue    # tells program to back to top of loop 
    print(letter)

my_string = "Oliver"
for letter in my_string:
    if letter == 'v':
        break    # breaks out of loop
    print(letter)
