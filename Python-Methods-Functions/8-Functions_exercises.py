# Write a function that returns the lesser of two given numbers if both numbers are even
# but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
            if a <= b:
                return a 
            elif b <= a:
                return b 
    elif a%2 != 0 or b%2 != 0:
        if a >= b:
            return a
        if b >= a:
            return b

""" 
''' Ideal solution '''
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
"""

print(lesser_of_two_evens(8,4))
print(lesser_of_two_evens(1,7))

# Write a function takes a two-word string and returns 
# True if both words begin with same letter

def animal_crackers(text):
    split_text = text.split()
    if split_text[0][0].lower() == split_text[1][0].lower():
        print("Both words begin with the same letter")
        return True
    else:
        print("Both words begin with different letters")
        return False

""" 
''' Ideal solution '''
def animal_crackers(text):
    split_text = text.lower().split()
    return split_text[0][0] == split_text[1][0]
"""

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

# Given two integers, return True if the sum of the integers 
# is 20 or if one of the integers is 20. If not, return False

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20:
        print("One of the values equals 20")
        return True
    elif n1 + n2 == 20:
        print("The sum of the values is 20")
        return True
    else:
        print("The sum of values doesn't equal 20")
        return False

""" 
''' Ideal solution '''
def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or n1 + n2 == 20:
        return True
    else:
        return False
"""

makes_twenty(5,20)
makes_twenty(14,6)
makes_twenty(2,3)