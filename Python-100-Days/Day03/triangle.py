import math

# print(math.sqrt(3))
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and b + c > a and c + a > b:
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("The area of triangle is %.3f" % area)
else:
    print("a, b, c can't build a triangle")
