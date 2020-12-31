# useful operators
my_list = [1,2,3,4,5]
for number in range(0,11,2):    # range is a generator 
     print(number)

my_new_list = list(range(0,11,2))
print(my_new_list)

# Built in enumerate function 
my_string = "Oliver"
# Creates a tuple with the index and the character
for letter in enumerate(my_string):
    print(letter)
# tuple unpacking can assist with this 
for index, letter in enumerate(my_string):
    print(f"index: {index} -- letter: {letter}")

# Zip function - zip only works up to shortest list 
my_list = [1,2,3]
my_list2 = ['a', 'b', 'c']
for item in zip(my_list, my_list2): # cast to list if you want a list of tuples
    print(item)

# in operator works on dictionaries (for keys) lists, strings and more
x_in = 'x' in [1,2,3]
print(x_in)
x_in = 'x' in ['x',2,3]
print(x_in)

# User input function
# input will always accept user input as a string
x = input("Please enter a number:")
# cast to a particular data type can be done above int(input())
print(type(int(x)))