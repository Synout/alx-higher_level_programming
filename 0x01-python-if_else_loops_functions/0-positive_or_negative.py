#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number == 0:
    print("{} is zero".format(number))
else:
    sign = "negative" if number < 0 else "positive"
    print("{} is {}".format(number, sign))
