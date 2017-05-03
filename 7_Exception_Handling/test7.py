my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
except KeyError:
    print("a KeyError occurred!")
finally:
    print("the finally statement has executed!")