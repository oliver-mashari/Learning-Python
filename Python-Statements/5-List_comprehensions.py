my_string = 'hello'

my_list = [] 
for letter in my_string:
    my_list.append(letter)
    print(f"Contents of list: {my_list}") 

# More efficent way of doing the above 
# lets break down the above for loop into a list comprehension
my_string = "world"
my_list = [letter for letter in my_string]  # essentially a flattened out for loop - letter is a temp name
print(f"Contents of list: {my_list}") 
my_list = [num for num in range(0,101,5)]
print(f"Contents of list: {my_list}") 
my_list = [num*3 for num in range(0,101,5)] # appending first num into the list so it can be subject to some numerical operator for example
print(f"Contents of list: {my_list}") 
# list of even numbers
my_list = [num for num in range(0,101,5) if num % 2 == 0] # appending first num into the list so it can be subject to some numerical operator for example
print(f"Contents of list: {my_list}") 

# See python course notes for if else statements with list comprehension
# nested loops as well but this can also be quite confusing 

