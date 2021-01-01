# *args = arguments 
# *kwargs = keyword arguemnts

"""
def myfunc(x,y):
    # Returns 5% of the sum of x and y
    return sum((x,y)) * 0.05
"""

# *args allows an arbitrary number of arguements to be passed in
def myfunc(*args):
    return sum(args) * 0.05

result = myfunc(10,10,10,10,10,10,10)
print(result)

# **kwargs allows an arbitrary number of key worded arguments
def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print("No fruit here")

myfunc2(fruit='apple',vegetable='mushroom')

# args and kwargs can be used together 
def myfunc3(*args,**kwargs):
    print(f"I would like {args[0]} {kwargs['food']}")

myfunc3(10,20,30,food='chinese', animal='cat', colour='red')

# coding exercise 18 check 
def func(*args):
    mylist = []
    for values in args:
        if values % 2 == 0:
            mylist.append(values)
    return mylist

result = func(1,2,3,4,5,6)
print(result)

# coding exercise 19 check 
# My solution 
def func(*args):
    newword = ''
    counter = 1
    for word in args:
        for letter in word:
            if counter % 2 == 0:
                letter = letter.upper()
            else:
                letter = letter.lower()
            counter += 1
            newword += letter 
        return newword
result = func('new')
print(result)

# coding exercise 19 check 
# Exercise solution 
def mfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

result = mfunc('supercalifragilisticexpialidocious')
print(result)