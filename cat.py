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
        self.age += 1

    def eat(self):
        print(f"{self.name} +  will now eat ")
        self.energy += 10
        self.weight += 10
        self.age += 1
    
    def sleep(self):
        print(f"{self.name} + is now sleeping")
        self.energy += 10
        self.weight -= 5
        self.age += 1

    def stats(self):
        print(f"{self.name}\n Colour:{self.colour} \nAge: {self.age}\n Energy: {self.energy}\n Intelligence: {self.weight}")

    
    def create(self):
