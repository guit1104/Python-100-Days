inch_len = float(input("Please type in value of length: "))
unit = input("Please input length unit: ")

if unit == 'in':
    print('%f inch = %f cm' % (inch_len, inch_len * 2.54))
elif unit == 'cm':
    print('%f cm = %f in' % (inch_len / 2.54, inch_len))
else:
    print('please input valid unit.')
