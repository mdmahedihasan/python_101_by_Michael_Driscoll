def function_a():
    global a
    a = 1
    b = 2
    return a + b


def function_b():
    c = 3
    return a + c

print(function_a())
print(function_b())