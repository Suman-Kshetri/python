# A generator is a simple way to build an iterator with yield.
# It saves memory because it produces values only when needed.

def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

print("Squares up to 10:")
for square in squares(10):
    print(square)