def gcd(x, y):
    # while y != 0:
    #     t = y
    #     y = x % y
    #     x = t
    while y != 0:
        (x, y) = (y, x % y)

    return x
def lcm(x, y):
    return x * y // gcd(x, y)

print(gcd(24, 30))
print(lcm(24, 30))

# if __name__ == '__main__':
#     main()
