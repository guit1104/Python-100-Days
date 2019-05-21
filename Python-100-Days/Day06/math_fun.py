print(chr(97))
print(hex(ord('Z')))
print(abs(-1.234))
print(round(-1.234, 2))
print(pow(1.2345, 5))


fruits = ['orange', 'peach', 'durian', 'watermelon']

print(fruits[1:3])
print(fruits[slice(1,3)])

def myfilter(mystr):
    return len(mystr) == 6

fruits2 = list(filter(myfilter, fruits))

print(fruits)
print(fruits2)
