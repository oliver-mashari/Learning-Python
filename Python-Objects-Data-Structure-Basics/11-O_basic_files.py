# Simple input and output in python 
# full file path needed unless working in jupyter notebooks 
# r"" no need for \\ in path 
file_path = r"C:\Users\ollie\Desktop\Python Course\Learning-Python\Python-Objects-Data-Structure-Basics\basic.txt"
my_file = open(file_path)
print(my_file.read())
# this returns nothing 
# think of it like thge cursor being at the end of the file it needs 
# to be reset to beginning of the file to read the file again
print(my_file.read())
my_file.seek(0)     # Resets 'cursor'
print(my_file.read())
# breaking text file into list of lines
my_file.seek(0)     # Resets 'cursor'
lines = my_file.readlines()
print(lines)
# close file 
my_file.close()


# reading, appending and writing 
# basic reading mode same as abopve 
with open(file_path,mode='r') as my_new_file:
    contents = my_new_file.read()
print(contents)
# basic appending after appending file needs to be open in read mode 
with open(file_path,mode='a') as my_new_file:
    my_new_file.write('\nThis is the fourth line of this file')
with open(file_path,mode='r') as my_new_file:
    contents = my_new_file.read()
print(contents)
# basic write (will overwrite file)
file_path_new = r"C:\Users\ollie\Desktop\Python Course\Learning-Python\Python-Objects-Data-Structure-Basics\new_file.txt"
with open(file_path_new,mode='w') as my_new_file:
    my_new_file.write('I made this')
