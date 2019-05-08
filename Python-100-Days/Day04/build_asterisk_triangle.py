rows = int(input("Please input number of triangle rows:"))

#first triangle
for i in range(rows):
    for _ in range(i + 1):
        print('*', end='')
    print()

#secnd triangle
for i in range(rows):
    for j in range(rows):
        if j < rows - 1 - i:
            print(' ', end='')
        else:
            print('#', end='')
    print()


for i in range(rows):
    for j in range(rows - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('&', end='')
    print()
