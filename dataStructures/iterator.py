# An iterator lets you loop through items one by one.
# It remembers where it is, so it uses less memory

aList = [1, 2, 3, 4, 5]

it = iter(aList)

# print(next(it))  # Output: 1
# print(next(it))  # Output: 2
# print(next(it))  # Output: 3
# print(next(it))  # Output: 4
# print(next(it))  # Output: 5

# Using a for loop to iterate through the list

print("using for loop:")
while True:
    try:
        num = next(it)
        print(num)
    except StopIteration:
        break


