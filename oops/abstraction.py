# Abstraction = hiding implementation details
# Show only essential features
# Achieved using:
# Abstract classes (abc module)
# Abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with button")

# Usage
c = Car()
c.start()

b = Bike()
b.start()