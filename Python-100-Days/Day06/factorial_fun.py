def factorial(n):
    res = 1
    for num in range(1, n + 1):
        res *= num
    return res

if __name__ == '__main__':
    print(factorial(7) // factorial(3) // factorial(4))
