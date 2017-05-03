try:
    file_handler = open("test.txt")
    for line in file_handler:
        print(line)
except IOError:
    print("an IOError has occurred!")
finally:
    file_handler.close()