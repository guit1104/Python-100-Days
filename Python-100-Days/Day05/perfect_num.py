import math
import time
# val = int(input('num = '))
#
# num = 0
start = time.clock()

for val in range(1, 100000):
    num = 0
    for x in range(1, int(math.sqrt(val)) + 1):
        if val % x == 0:
            num += x
            if x > 1 and val / x != x:
                num += val / x

    if num == val:
        print('%d is perfect num' % val)
    # else:
    #     print('not perfect num')

end = time.clock()

print('running time is %d second' % (end - start))
