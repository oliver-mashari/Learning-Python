# Equlaity operator
int_comp = 2 == 2
print(int_comp)
int_comp2 = 2 == 1
print(int_comp2)
string_comp = "hello" == "bye"
print(string_comp)
string_comp2 = "Bye" == "bye"     # Capatalisation matters
print(string_comp2)
type_comp = '2' == 2              # Will return FALSE
print(type_comp)
float_comp = 2.0 == 2             # Will return TRUE as they are the same value
print(float_comp)

# Inequlaity operator - same as above except different operator 
int_comp = 3 != 3
print(int_comp)
int_comp = 4 != 3
print(int_comp)

# Similar usage for greater, less, greater equal, less equal 