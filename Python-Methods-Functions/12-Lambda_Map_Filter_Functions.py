# Lambdas, map and filter

# we first need a function to use with map 
def square(num):
    return num**2
my_nums = [1,2,3,4,5]

# map returns a memory location
print(map(square,my_nums))

# iterate through map to get items
for item in map(square,my_nums):
    print(item)

# You can also get a list back 
print( list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['bob', 'lola', 'derek']
print(list(map(splicer,names)))

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]
print(list(filter(check_even,mynums)))

# Lambda expression 
squarenum = lambda num: num ** 2
print(squarenum(3))
print(list(map(lambda num: num**2, mynums)))