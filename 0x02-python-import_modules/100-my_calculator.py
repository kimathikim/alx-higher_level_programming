#!/usr/bin/python3
import sys
from calculator_1 import *


def main():
    result = 0
    if (len(sys.argv) != 3):
        print("./100-my_calculator.py a operator b")
        exit(1)

    a = int(sys.argv[1])
    sign = int(sys.argv[2])
    b = int(sys.argv[3])
    if sign == '+':
        result = add(a, b)
        print("{} {} {} = {}".format(a, argv[2], b, result))
    elif sign == '-':
        result = sub(a, b)
        print("{} {} {} = {}".format(a, argv[2], b, result))
    elif sign == '*':
        result = mul(a, b)
        print("{} {} {} = {}".format(a, argv[2], b, result))
    elif sign == '/':
        result = div(a, b)
        print("{} {} {} = {}".format(a, argv[2], b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
