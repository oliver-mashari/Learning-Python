# Basic dictionaries 
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(my_dict['key1'])

price_lookup = {'apple':2.99, 'orange':0.99, 'bananas':0.50}
print(price_lookup['apple'])

# Nested dictionaries 
d = {'value':1, 'd_list':[0,10,20], 'd_nest':{'insideKey':100}}
print(d)
print(d['d_list'])
print(d['d_list'][2])
print(d['d_nest']['insideKey'])

# Add new key value pair to dictionary 
price_lookup['bread'] = 1.99
print(price_lookup)

# methods 
print(d.values())
print(d.keys())