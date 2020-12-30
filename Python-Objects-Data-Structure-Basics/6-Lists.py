# lists and list object types
my_list     = [1,2,3,4,5] # list of ints
my_list2    = ['String', 3, 21.5] # mixed object types
print(my_list)
print(my_list2)
print('list length:', len(my_list2))    # check length of list

# list indexing 
print(my_list[1])
print(my_list[2:])

# List cocatenation 
another_list = [6,7,8]
new_list = my_list + another_list
print(new_list)

# Lists are mutable - mutating lists
new_list[0] = "one"
print(new_list)

# List methods 
new_list.append('nine')
print(new_list)
pop = new_list.pop()    # pop supports indexing 
print(pop)
print(new_list)
random_list = [1, 4, 10, 3, 2, 6, 7]
random_list.sort()  # this occurs in place can't be assigned to a variable 
print(random_list)

# Nested list indexing
nested_list = [1,2,[3,4]]
print(nested_list[2][1])