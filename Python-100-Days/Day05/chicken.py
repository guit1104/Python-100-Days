#each cock is $5, each hen is $3, 3 chicken are $1, given $100, we want to buy 100 chicken, how many amount for each?

for x in range(100 // 5 + 1):
    for y in range(100 // 3 + 1):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('%d, %d, %d' % (x, y, z))
