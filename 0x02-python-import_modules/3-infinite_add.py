#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = 0
    for i in argv[1:]:
        n += int(i)
    print("{:d}".format(n))
