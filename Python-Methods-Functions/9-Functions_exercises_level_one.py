# Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    newName = []
    # Enumarate assigns each character an index and stores in a tuple
    # tuple unpacking
    for index,letter in enumerate(name):
        if index == 0 or index == 3:
            letter = letter.upper()
        newName.append(letter)
    return ''.join(newName)

""" 
''' Ideal Solution '''
def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capatalize() + second_half.capatalize()  
"""

print(old_macdonald('macdonald'))

# Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    new_sentence = text.split()
    new_sentence.reverse()
    return ' '.join(new_sentence)

""" 
''' Solution from lecture '''
def master_yoda(text):
    my_list = text.split()
    reversed_list = my_list[::-1]
    return ''.join(reversed_list)
"""

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

# Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    if n in range(90, 111,1) or n in range(190,210,1):
        return True
    else:
        return False


"""
''' Solution from slides '''
def almost_there(n):
    return abs((100-n <= 10) or abs((200-n) <= 10)
"""
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))