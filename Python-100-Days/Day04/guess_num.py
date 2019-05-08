import random

answer = random.randint(1, 100)
count = 0

while True:
    count += 1
    val = int(input("Guess a number: "))

    if val < answer:
        print("Your guess is a litter low")
    elif val > answer:
        print("Your guess is a litter high")
    else:
        print("Bingo!!!")
        break

if count > 7:
    print("You're such a fool!\n ;)")
