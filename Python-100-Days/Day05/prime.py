import math

for num in range(2, 100):
    prime = True

    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            prime = False
            break
    if prime:
        print(num, end=' ')
