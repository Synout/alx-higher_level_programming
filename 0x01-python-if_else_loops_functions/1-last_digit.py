#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = -1 if number < 0 else 1
last_d = int(str(number)[-1])*sign

if last_d == 0:
    print("Last digit of {} is {} and is 0".format(number, last_d))
elif last_d > 5:
    print("Last digit of {} is {} and greater than 5".format(number, last_d))
elif last_d < 6 and last_d != 0:
    print("Last digit of {} is {} and less than 6 and not 0".format(number, last_d))
