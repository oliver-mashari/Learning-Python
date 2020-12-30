# Single and double quotes 
single = 'hello'
double = "world"

print(single, double)

# Single and double quotes can be used in same string 
sent = "I'm going on holiday"
print(sent)

# Indexing and Slicing 
myString = "Hello World"
print(myString[0])
print(myString[8])
print(myString[-1])     # reverse indexing 

myString = "abcdefghijk"
print(myString[2:])     # Starts at second index and slices to the end
print(myString[:3])     # Stop goes upto but not including this will exclude the character 'd'
print(myString[3:6:1])

# Reverse a string 
# RATHER THAN WRITING A FOR LOOP
print(myString[::-1])