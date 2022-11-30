#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = -1 if number < 0 else 1
last_d = int(str(number)[-1])*sign
txt = "Last digit of {} is {} and ".format(number, last_d)
if last_d == 0:
    print("{}is 0".format(txt))
elif last_d > 5:
    print("{}is greater than 5".format(txt))
elif last_d < 6 and last_d != 0:
    print("{}is less than 6 and not 0".format(txt))
