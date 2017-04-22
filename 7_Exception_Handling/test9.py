my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["a"]
except KeyError:
    print("a KeyError occurred!")
else:
    print("no error occurred!")
finally:
    print("the finally statement ran!")