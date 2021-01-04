class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

# Lets inherite some of the animal methods 
# Into a new dog class
class Dog(Animal):
    def __init__(self):
        # All methods derived from animal 
        Animal.__init__(self)
        print("Dog created")
    # You can overwrite methods in animal
    def who_am_i(self):
        print("I am a dog")
    def bark(self):
        print("Woof!")

my_dog = Dog()
# my_dog.who_am_i()

# Polymorphism
