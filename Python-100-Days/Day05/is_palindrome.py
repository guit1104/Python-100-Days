val = int(input("num = "))

num, rev = val, 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if val == rev:
    print('%d is palindrome' % val)
else:
    print('not a palindrome')
