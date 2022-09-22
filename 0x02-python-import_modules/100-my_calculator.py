#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import *
    result = 0
    if (len(argv) != 3):
        print("./100-my_calculator.py a operator b")
        exit(1)
    for i in range(1, len(argv)):
        a = argv[1]
        sign = argv[2]
        b = argv[3]
    if sign == '+':
        result = add(int(a), int(b))
        print("{} + {} = {}".format(a,b, result))
    elif sign == '-':
        result = sub(int(a), int(b))
        print("{} - {} = {}".format(a,b, result))
    elif sign == '*':
        result = mul(int(a), int(b))
        print("{} * {} = {}".format(a,b, result))
    elif sign == '/':
        result = div(int(a), int(b))
        print("{} / {} = {}".format(a,b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
