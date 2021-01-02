# Imports
from IPython.display import clear_output
import random 

"""
Step 1: Write a function that can print out a board. Set up your board as a list, 
where each index 1-9 corresponds with a number on a number pad, 
so you get a 3 by 3 board representation.
"""
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

"""
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
Think about using while loops to continually ask until you get a correct answer.
"""
def player_input():
    player_marker = ''
    while player_marker != 'X' and player_marker != 'O':
        player_marker = input("Player one select X or O to play as: ").upper()
        if player_marker != 'X' and player_marker != 'O':
            print("Sorry this is not a valid choice")
    # Assign Markers
    player1 = player_marker
    if player1 == 'X':
        player2 = 'O'
    if player1 == 'O':
        player2 = 'X'
    return (player1, player2)

"""
Step 3: Write a function that takes in the board list object, a marker ('X' or 'O')
and a desired position (number 1-9) and assigns it to the board.
"""
def place_marker(board, marker, position):
    board[position] = marker

"""
Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
"""
def win_check(board, mark):
    # Check rows
    if ((board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[1] == mark and board[2] == mark and board[3] == mark)):
        return True
    # Check columns
    elif ((board[9] == mark and board[6] == mark and board[3] == mark) or
        (board[8] == mark and board[5] == mark and board[2] == mark) or
        (board[7] == mark and board[4] == mark and board[1] == mark)):
        return True
    # Check diagonals
    elif ((board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark)):
        return True

"""
Step 5: Write a function that uses the random module to randomly decide which player goes first. 
You may want to lookup random.randint() Return a string of which player went first.
"""
def choose_first():
    decision = random.randit(1,2)
    if decision == 1:
        return 'Player 1'
    else:
        return 'Player 2'

"""
Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
"""
def space_check(board, position):
    avaliability = False
    while avaliability == False:
        if board[position] == 'X' or board[position] == 'O':
            "Space not avaliable"
        else:
            avaliability = True

"""
Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
"""
def full_board_check(board):
    for i in range(len(1,board)):
        if board[i] == 'X' or board[i] == 'O':
            continue
        else:
            return False
    print("Board is full")
    return True

"""
Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function 
from step 6 to check if it's a free position. If it is, then return the position for later use.
"""
def player_choice(board):
    # Variables 
    # Initial choice 
    choice = "No"
    acceptable_range = range(1,9)
    within_range = False

    # Two conditions to check 
    # Digit or within range == False 
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number 0-9: ")
        # Digit check 
        if choice.isdigit() == False:
            print("Sorry this is not a digit")
        # range check 
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry outwith range")
                within_range = False 
   
    space_check(board,choice)

