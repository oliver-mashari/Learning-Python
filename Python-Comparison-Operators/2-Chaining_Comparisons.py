# If you want to make more one comparison at a time
# logical operators
and_op = 1 < 2 and 2 > 3    # False
print(and_op)
and_op = 1 < 2 and 2 < 3    # True
print(and_op)
or_op = 1 < 2 or 2 > 3      # True - only needs one of them to be true
print(or_op)
not_op = not 1 == 1         # True - Returns opposite so this will be False
print(not_op)