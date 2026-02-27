flag = True

with open("example.txt","w") as file:
    file.write("Hello world")
    while(flag):
        input_str = input("Enter data [or press N/n to exit: ")
        file.write("\n")
        if input_str == "N" or input_str == "n" :
            flag = False
        else:
            file.write(input_str)

with open("example.txt","r") as file:
    content = file.read()
    print(content)
