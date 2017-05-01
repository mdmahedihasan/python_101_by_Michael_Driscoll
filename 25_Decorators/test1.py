def another_function(func):
    """a function that accepts another function"""
    def other_function():
        val = "The result of %s is %s" % (func(), eval(func()))
        return val
    return other_function


@another_function
def a_function():
    """a pretty useless function"""
    return "1 + 1"


if __name__ == '__main__':
    value = a_function()
    print(value)
    # decorator = another_function(a_function)
    # print(decorator())