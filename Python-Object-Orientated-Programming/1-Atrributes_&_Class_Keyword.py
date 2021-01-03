
"""
# Create a new class
class Sample():
    pass
# create an instance of a class
my_sample = Sample()
"""

"""
class Dog():
    # __init__ is the class constructor
    def __init__(self,breed):
        # we take in the argument 
        # assign it using self.attribute_name
        # # self.breed is the attribute
        self.breed = breed

my_dog = Dog(breed='Pug')
print(my_dog.breed)
"""

class Dog():
    # __init__ is the class constructor
    def __init__(self,breed,name,spots):
        # we take in the argument 
        # assign it using self.attribute_name
        # # self.breed is the attribute
        self.breed = breed
        self.name = name
        # Expect boolean
        self.spots = spots
my_dog = Dog(breed='Pug',name='Doug',spots=False)
print(my_dog.breed, my_dog.name, my_dog.spots)
