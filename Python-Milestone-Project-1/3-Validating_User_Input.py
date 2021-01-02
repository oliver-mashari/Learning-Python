# No validation here I could enter 1000 and the function would accept it as the user inout
"""
def user_choice():
    choice = input("Please enter a number 0-9: ")
    return int(choice)
user_choice()
"""

def user_choice_while():
    # Variables 
    # Initial choice 
    choice = "No"
    acceptable_range = range(0,9)
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
    return int(choice)

user_choice_while()