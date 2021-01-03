from IPython.display import clear_output
import random

# Function to display board
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

# Ask player one which marker they would prefer to use
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

# Place marker on board
def place_marker(board, marker, position):
    board[position] = marker

# Win conditions
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

# Randomly select which player moves first 
def choose_first():
    decision = random.randint(1,2)
    if decision == 1:
        return 'Player one'
    else:
        return 'Player two'

# Check if space on board is occupied
def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True

# Check full board to determine if any more moves can be made 
# if not game ends in a tie
def full_board_check(board):
    for i in range(1,len(board)):
        if board[i] == 'X' or board[i] == 'O':
            continue
        else:
            return False
    print("Board is full")
    return True

# Ask player where they want to place marker
def player_choice(board):
    # Variables
    position = "No"
    acceptable_range = range(1,9)
    within_range = False
    space = False

    while position.isdigit() is False or within_range is False or space is False:
        position = input("Please enter a number 1-9: ")
        # Digit check 
        if position.isdigit() == False:
            print("Sorry this is not a digit")
        # Range check 
        elif position.isdigit() == True:
            if int(position) in acceptable_range:
                # Check if space is occupied
                if space_check(board, int(position)) == False:
                    print("Space not avaliable")
                    space = False
                else:
                    space = True
                within_range = True
            else:
                print("Sorry outwith range")
                within_range = False
    return int(position)

def replay():
    choice = ''
    while choice == 'Y' or choice == 'N':
        choice = input("Would you like to play again? (Y or N): ").upper()
        if choice == 'Y':
            return True
        else:
            return False

print('Welcome to Tic Tac Toe!')

while True:
    game_board = [' ']*10
    marker_p1, marker_p2 = player_input()
    player = choose_first()
    if player == 'Player one':
        print(f"{player} will make the first move playing as {marker_p1}")
    elif player == 'Player two':
        print(f"{player} will make the first move playing as {marker_p2}")
    start_game = input("Are you ready to play? (Y or N): ").upper()
    if start_game == 'Y':
        start_game = True 
    else:
        start_game = False
        
        
    while start_game is True:
        #Player 1 Turn
        if player == 'Player one':
            display_board(game_board)
            print(" ")
            print(" ")
            position = player_choice(game_board)
            place_marker(game_board, marker_p1, position)
            
            if win_check(game_board, marker_p1) == True:
                display_board(game_board)
                print(f"Congratulations {player}")
                start_game = False
            else:
                if full_board_check(game_board) == True:
                    display_board(game_board)
                    print("the game is a draw")
                    break
                else: 
                    player = 'Player two'
                
        # Player2's turn.
        else:
            display_board(game_board)
            print(" ")
            print(" ")
            position = player_choice(game_board)
            place_marker(game_board, marker_p2,position)
            
            if win_check(game_board, marker_p2) == True:
                display_board(game_board)
                print(f"Congratulations {player}")
                start_game = False
            else:
                if full_board_check(game_board) == True:
                    display_board(game_board)
                    print("the game is a draw")
                    break
                else: 
                    player = 'Player one'

    if not replay():
        break