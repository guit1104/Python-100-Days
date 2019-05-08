import math
for num in range(100, 1000):
    val, temp = 0, num
    while num != 0:
        val += int(math.pow((num % 10), 3))
        num //= 10
    if temp == val:
        print("%d" % (temp))
print("======")

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
