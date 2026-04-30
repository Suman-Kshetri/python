class Animals:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} Speaks !")

# derived class
class Dog(Animals): 
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        super().speak() # call the base class method
        print(f"{self.name} says Woof !")
        print(f"{self.name} is a {self.breed}")

dog1 = Dog("Buddy", "Golden Retriever")
dog1.speak()

class A:
    def show(self):
        print("A")
class B:
    def show(self):
        print("B")

class C(A, B): # -> when A is in first then A is printed
# class C(B, A): # -> when B is in first then B is printed
    pass
c1 = C()
c1.show()