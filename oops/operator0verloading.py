# operator overloading is one of concept of polymorphism in OOPs.

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def __str__(self):
        return f"{self.real} + {self.img}j"
    
    def __add__(self, other):
        # if not isinstance(other, Complex):
        #     return NotImplemented
        real = self.real + other.real
        img = self.img + other.img
        return Complex(real, img)

c1 = Complex(2, 3)
c2 = Complex(4, 5)
complex_sum = c1 + c2
print(f'Sum of {c1} and {c2} is {complex_sum}')