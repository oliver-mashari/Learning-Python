""" syntax of a for loop
my_iterable = [1,2,3]
for item_name in my_iterable:   # item_name is a variable name
    print(item_name)
"""
# Iterating through lists of integers
my_list = [1,2,3,4,5,6,7,8,9,10]
for list_entry in my_list:
    # Check for even numbers
    if list_entry % 2 == 0:   
        print(f"Even Number: {list_entry}")
    else:
        print(f"Odd number {list_entry}")

list_sum = 0
for number in my_list:
    list_sum = list_sum + number
    print(f"loop {number} sum: {list_sum}")
print(f"Final value: {list_sum}")

# Iterate through string characters
my_string = "Hello World"
for letters in my_string:   # Will also print whitespace
    print(letters)

# Tuple unpacking
my_list_tup = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for item in my_list_tup:
    print(item)
for (a,b) in my_list_tup:   # if print(a) is called in for loop the first object of each tuple is printed to the console
    print(f"first index of each tuple: {a}")

# Dictionary iteration 
my_dict = {"k1":1 , "k2":2 , "k3":3}
for value in my_dict:
    print(value)     # this will iterate through the keys 
for value in my_dict.values():  # use the .values or .items method to get dictionary values 
    print(value)
# Alternatively to the above
for key,value in my_dict.items():
    print(f"Dictionary: {key}")
    print(f"Dictionary: {value}")

