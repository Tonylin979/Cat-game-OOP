#Our Cat entity
class Cat:
    def __init__ (self, given_name, given_colour):
        #The constructor - creates a instance of a class
        # - To create the cat, we need a given_name & given_colour
        self.name = given_name
        self.colour = given_colour
# an Instance of Cat
# An instance is a specific occurrence of a class
mimi = Cat("Mimi", "Brown")
print(mimi.name)
print(mimi.colour)