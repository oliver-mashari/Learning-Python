# sets in python
my_set = set()
print(my_set)
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
# this won't do anything as 2 is already in set 
# sets need to contain unique values 
# see list example
my_set.add(2) 
print(my_set)
my_list = [5,5,2,2,2,4,4,4,6,6,6,1,1]
print(set(my_list))


