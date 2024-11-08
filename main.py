#Our Cat entity
from cat import Cat

# An instance is a specific occurrence of a class
mimi = Cat("Mimi", "Brown")
mimi.train()

asta = Cat("Asta", "Black")

print(mimi.energy)
print(asta.energy)