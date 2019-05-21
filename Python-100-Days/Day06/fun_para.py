def f1(a, b=5, c=10):
    return a + b*2 + c * 3
#default argument
print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c = 2, b = 3, a = 1))


#varialbe length arguments
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


#keyword varialbe length of arguments
def f3(**kw):
    if 'name' in kw:
        print('Hello %s' % kw['name'])
    elif 'tel' in kw:
        print('your phone number is %s!' % kw['tel'])
    else:
        print('your info no found')

param = {'name': 'gui', 'age': 32}
f3(**param)
f3(usr='gui', age = 33, tel='31314')
