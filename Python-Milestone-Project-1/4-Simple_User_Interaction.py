# Lets build a simple game
game_list = [0,1,2]
# Display game list
def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

# Position choice 
def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2,): ")
        if choice not in ['0', '1','2']:
            print("Sorry, invalid choice!")
    return int(choice)

# Replacement choice updates game list 
def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list

def game_on():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Keep playing (Y or N): ")
        if choice not in ['Y','N']:
            print("Sorry, please choose Y or N")
    if choice == "Y":
        return True
    elif choice == "N":
        return False

game_on_type = True
game_list = [0,1,2]

while game_on_type:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    display_game(game_list)
    game_on_type = game_on()