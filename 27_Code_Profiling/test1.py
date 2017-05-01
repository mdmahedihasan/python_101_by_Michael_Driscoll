import time


def fast():
    print("i run fast!")


def slow():
    time.sleep(3)
    print("i run slow!!!")


def medium():
    time.sleep(0.5)
    print("i run a little slowly...")


def main():
    fast()
    slow()
    medium()


if __name__ == '__main__':
    main()