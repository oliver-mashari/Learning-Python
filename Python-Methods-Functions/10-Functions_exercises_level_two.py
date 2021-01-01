# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        elif nums[i] == 3 and nums[i+1] != 3:
            return False

""" 
''' Ideal Solution '''
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
""" 

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    new_string = []
    for chars in text:
        new_string.append(chars*3)
    return ''.join(new_string)

""" 
''' Ideal Solution '''
def paper_doll(text):
    result = ''
    for char in text:
        result = char*3
    return result
""" 

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# Given three integers between 1 and 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    if a+b+c <= 21:
        return f'total: {a+b+c}'
    elif a+b+c > 21 and a == 11 or b == 11 or c == 11:
        sum = a+b+c - 10 
        if sum > 21:
            return f'BUST, total: {sum}'
    else:
        return f'BUST, total:{a+b+c}'

""" 
''' Ideal Solution '''
def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c]) - 10
    else:
        return 'BUST' 
""" 

print(blackjack(5,6,7))
print(blackjack(11,11,11))
print(blackjack(9,9,10))

# Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    total = 0
    for num in arr:
        if num >= 6 and num <= 9:
            continue
        else:
            total = total + num
    return total

""" 
''' Ideal Solution '''
def summer_69(arr):
    total = 0 
    add = True 
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break 
             else:
                 add = True
                 break
    return total
""" 

print(summer_69([1, 3, 5]))
print(summer_69([4, 4, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
