class DecoratorTest(object):
    """test regular method vs @classmethod vs @staticmethod"""
    def __init__(self):
        """constructor"""
        pass

    def doubler(self, x):
        print("running doubler")
        return x * 2


    @classmethod
    def class_tripler(klass, x):
        print("running tripler : %s" % klass)
        return x * 3


    @staticmethod
    def static_quad(x):
        print("running quad")
        return x * 4


if __name__ == '__main__':
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(DecoratorTest.class_tripler(3))
    print(DecoratorTest.static_quad(4))
    print(decor.static_quad(4))

    print(decor.doubler)
    print(decor.class_tripler)
    print(decor.static_quad)