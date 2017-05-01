def dubler(a):
    result = a * 2
    print(result)
    return result


def main():
    for i in range(1, 10):
        dubler(i)


if __name__ == '__main__':
    main()