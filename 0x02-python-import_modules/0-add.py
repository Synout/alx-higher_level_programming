'''
#!/usr/bin/python3

from add_0 import add
if __name__ == "__main__":
    a = 1
    b = 2

    print(f"{a} + {b} = {add(a, b)}")
'''

#!/usr/bin/python3


if __name__ == '__main__':
    from add_0 import add

    a = 1
    b = 2
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
