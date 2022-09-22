#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv) == 1):
        print("{} argument.".format((len(argv) - 1)))
    else:
        print("{} argument:".format((len(argv) - 1)))
    for i in range(len(argv)):
        if (i > 0):
            print("{}: {}".format((i), (argv[i])))
