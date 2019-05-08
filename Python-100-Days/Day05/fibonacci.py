
prev, cur = 0, 1
for _ in range(20):
    # temp = cur
    # cur += prev
    # prev = temp
    print('%d' % (cur), end = ' ')
    (prev, cur) = (cur, prev + cur)
