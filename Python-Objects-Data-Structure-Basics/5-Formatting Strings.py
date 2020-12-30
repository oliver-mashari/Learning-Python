# FORMATTING STRINGS .format()
print('This is a string {}' .format('INSERTED'))
# This just formats in order
print('The {} {} {}' .format('girl', 'is', 'happy'))
# Can use indexing 
print('The {2} {0} {1}' .format('girl', 'is', 'happy'))
# keywords can be assigned to the words
print('{gender} {colour} {shape} {item}' .format(item='ball',colour='blue',shape='square',gender='male'))

# FLOAT FORMATTING {value:width.precision f}
result = 100 / 777
print("The result was {r:1.3}" .format(r=result))   # 3 decimal point formatting
print("The result was {r:1.5}" .format(r=result))   # 5 decimal point formatting

# formatted string literals or f-strings
# this is used in the flex writer 
name = 'Oliver'
print(f'Hello my name is {name}')