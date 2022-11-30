#!/usr/bin/python3
for i in range(1, 27):
    if "{}".format(chr(ord('`') + i)) not in 'qe':
        print("{}".format(chr(ord('`') + i)), end='')
