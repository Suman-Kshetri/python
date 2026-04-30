#writing to a file
flag = True

with open("file/file.txt","w") as file:
    while(flag):
        input_str = input("Enter a string to write to the file (or 'exit' to stop): ")
        if input_str.lower() == 'exit':
            flag = False
        else:
            file.write(input_str + "\n")

#reading from a file
with open("file/file.txt","r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)