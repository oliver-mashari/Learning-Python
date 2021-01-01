# Logic with functions

"""
def even_check(number):
    # Below line not necessary 
    result = number % 2 == 0
    return result 
"""

# Most efficent way to return an even check in this case 
"""
def even_check(number):
    return number % 2 == 0
"""

# Return true or false if any number is even or not inside a list
my_list = [1,5,3,101,41,37,57,7]
"""
def even_check(list_numbers):
    for number in list_numbers:
        if number % 2 == 0:
            return True
        else:
            return False    # This is wrong 
            pass
    return False 
"""

my_list = [0,1,2,3,4,5,6,7,8,9,10]
# return number and boolean output 
def even_check(list_numbers):

    # placeholder variables 
    even_numbers = []

    for number in list_numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

check = even_check(my_list)
print(f"The result is {check}")