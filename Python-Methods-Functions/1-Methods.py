my_list = [1,2,3,4,5]
my_list.pop()   # this is a method 

# How to get the list of methods 
# just type out the method and help shjould appear 
# in jupyter notebooks hit shift+tab after insert* when the cursor is at the *
my_list.insert(2,6)
print(my_list)

# Another way to view help
# will return the docstring to the terminal
help(my_list.insert)    # method doesn't need () 