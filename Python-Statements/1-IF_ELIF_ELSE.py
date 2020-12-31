""" syntax of a if statement 
    if some_condition:
        # execute some code 
"""
if 3>2:
    print("It's True")
hungry = True 
if hungry == True:
    print("It's true, NOW FEED ME!")

""" syntax of a if statement 
    if some_condition:
        # execute some code 
    else:       # No condition needed only executes if above conditions are not met
        # execute some code
"""
hungry = False 
if hungry == True:
    print("It's true, NOW FEED ME!")
else:
    print("It's false, I'm not hungry...")

""" syntax of a if statement 
    if some_condition:
        # execute some code 
    elif some_condition:    # There can be as many elifs as you want
        # execute some code 
    else:       # No condition needed only executes if above conditions are not met
        # execute some code
"""
loc = "game"
if loc == "auto shop":
    print("I don't like cars")
elif loc == "bank":
    print("Money makes the world spin")
elif loc == "store":
    print("How may I help you today?")
else:
    print("I don't know")