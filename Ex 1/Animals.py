class Animal:

    def __init__(self, name, type, colour):
        self.name = name
        self.type = type
        self.colour = colour

    def move(self):
        print(f"{self.name} zmienił swoje położenie")

    def eat(self):
        print(f"{self.name} jest głodny")

cat = Animal("Kot Pusia", "ssak", "biały")

print(cat)
print(cat.name)
print(cat.type)
print(cat.colour)

dog = Animal("Pies Azor", "ssak", "czarny")

print(dog)
print(dog.name)
print(dog.type)
print(dog.colour)

cat.eat()
cat.move()

dog.eat()
dog.move()