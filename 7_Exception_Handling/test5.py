my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
except IndexError:
    print("this index does not exist!")
except KeyError:
    print("this key is not in the dictionary!")
except:
    print("some other error occurred!")