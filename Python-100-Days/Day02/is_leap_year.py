year = int(input("Please input year: "))

is_leap_year = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

print("is %d a leap year" % (year), is_leap_year, end="\n")
