class Cat:
    def __init__ (self, given_name, given_colour):
        #The constructor - creates a instance of a class
        # - To create the cat, we need a given_name & given_colour
        self.name = given_name
        self.colour = given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5
    
    def train(self):
        print(f"{self.name} is training.. ")
        self.intelligence += 1
        self.energy -= 5