# Three cup monte example 
# Illustrating how functions interact with each other

# How to shuffle a list with shuffle function 
from random import shuffle
"""
my_list = [1,2,3,4,5,6,7]
shuffle(my_list)    # inline function 
print(my_list)
"""

# define a function that shuffles a list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist 

"""
result = shuffle_list(my_list)
print(result)
"""

# Three cup monte example shuffle_list function will be used 

# define a function that returns the players guess
def player_guess():

    # place holder variables 
    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1, 2: ")

    return int(guess)

# define function to check guess
def check_guess(cups,guess):
    if cups[guess] == '0':
        print("Correct!")
        print(cups)
    else:
        print("Wrong!")
        print(cups)

# Cleaner example of it all together 
# Initalise list - setup cup and ball
my_list = ['','0','']
# Shuffle list 
shuffled_list = shuffle_list(my_list)
# User Guess
guess = player_guess()
# Check Guess
check_guess(shuffled_list, guess)