import sys

def main():
    f = [x for x in range(1, 10)]
    print(f)

    f = [x + y for x in 'ABCDE' for y in '123456']
    print(f)

    f = [x**2 for x in range(1, 1000)]
    print(sys.getsizeof(f))
    print(f)

    for val in f:
        print(val)
if __name__ == '__main__':
    main()
