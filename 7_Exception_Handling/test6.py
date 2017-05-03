my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
except(IndexError, KeyError):
    print("an IndexError or KeyError occurred!")