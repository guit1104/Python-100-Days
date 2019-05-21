
def main():
    str1 = 'hello, world!'
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())
    print(str1.find('or'))
    print(str1.center(20, '*'))

    str2 = 'abc1234'
    print(str2[::-1])
    print(str2[-3:-1])
    print(str2.isdigit())
    print(str2.isalnum())
if __name__ == '__main__':
    main()
