class DataError(Exception):
    pass

def get_integers():
    aList = []

    while True:
        try:
            s = input("Enter integer [q to quit]: ")

            if s == 'q':
                break
            
            try:
                n = int(s)

            except:
                raise DataError("Invalid integer input")
            
            aList.append(n)
        except DataError as e:
            print(f"Caught Exception: {e}")
    return aList

list=get_integers()
print("List of data is: ",list)
