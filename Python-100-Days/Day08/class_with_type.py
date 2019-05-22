def bar(self, name):
    self._name = name

def foo(self, course_name):
    print('%s is studying %s.' % (self._name, course_name))

def main():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    stu1 = Student('Gui')
    stu1.study("Python coding")

if __name__ == '__main__':
    main()
