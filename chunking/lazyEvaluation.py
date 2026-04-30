def read_line(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line

for line in read_line("data.txt"):
    print(line)