# A lambda is a small, anonymous function.
# You use it when you need a simple function for a short time.

# 1. Use case 1: sorting
data = [(1, "Ram", "Biratnagar" ), (2, "Shyam", "Ithari"), (3, "Rjesh","Dharan"), (4, "Hari", "Biratnagar")]
# Sort by address
sorted_data = sorted(data, key=lambda x: x[2])
print(f'Sorted by address: {sorted_data}')
# sort by name
sorted_data = sorted(data, key=lambda x: x[1])
print(f'Sorted by name: {sorted_data}')
# without lambda
def get_address(x):
    return x[2]
sorted_data = sorted(data, key=get_address)
print(f'Sorted by address without lambda: {sorted_data}')

# 2. Use case 2: maping
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f'Squared numbers: {squared}')

# without lambda
def square(x):
    return x**2
squared = list(map(square, numbers))
print(f'Squared numbers without lambda: {squared}')

# 3. Use case 3: filtering
num = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, num))
print(f'Even numbers: {even_numbers}')

# without lambda
def is_even(x):
    return x % 2 == 0
even_numbers = list(filter(is_even, num))
print(f'Even numbers without lambda: {even_numbers}')