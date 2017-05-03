try:
    with open("test.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("an IOError has occurred!")