#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul


def main():
    result = 0
    if (len(sys.argv) != 3):
        print("./100-my_calculator.py a operator b")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if argv[2] == '+':
        result = add(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
    elif argv[2] == '-':
        result = sub(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
    elif argv[2] == '*':
        result = mul(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
    elif argv[2] == '/':
        result = div(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
