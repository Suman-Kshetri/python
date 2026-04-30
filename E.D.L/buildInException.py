#value error
try:
    number = int("not a number")
except ValueError as e:
    print(f"value error: {e}")

# file not found error 
# specific exception handling
try:
    with open("file.txt","r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"File not found : {e}")

# general exception handling
try:
    with open("file.txt","r") as file:
        content = file.read()
except Exception as e:
    print("Exception orccured:", e )

#index error
try:
    my_list = [1,3,7,8]
    print(my_list)
    print(my_list[10])
except IndexError as e:
    print(f"index error: {e}")
