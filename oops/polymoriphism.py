# The same method/function name behaves differently depending on the object.
# Same method in parent & child class
# Child class changes behavior

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()