# Dog class from previous lecture 

# class Dog():

#     # CLASS OBJECT ATTRIBUTE
#     # SAME FOR ANY INSTANCE OF A CLASS
#     species = 'mammal'

#     def __init__(self,breed,name):
#         # we take in the argument 
#         # assign it using self.attribute_name
#         # # self.breed is the attribute
#         self.breed = breed
#         self.name = name

#     def bark(self):
#         print(f"Woof! My name is {self.name}")

# # species doesn't need to passed in as an argument 
# # it is local to the class
# my_dog = Dog('German Shepard','Millie')
# # species will be avaliable as an attribute 
# print(my_dog.species)
# my_dog.bark()


class Circle():

    # Class object attribute
    pi = 3.14 

    def __init__(self,radius=1):
        self.radius = radius 
        # An attribute doesn't need to be defined by parameter call 
        self.area = radius**2 * self.pi

    # Method 
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(10)
print(my_circle.pi, my_circle.radius, my_circle.area)
print(my_circle.get_circumference())
