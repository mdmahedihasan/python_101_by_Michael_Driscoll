my_list = [1, 2, 3, 4, 5]

try:
    my_list[6]
except IndexError:
    print("that index is not in the list!")