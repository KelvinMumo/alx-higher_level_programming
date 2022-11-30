#!/usr/bin/python3
for i in range(0, 100):
    dig1 = i / 10
    dig2 = i % 10
    if i == 89:
        print("{:d}".format(i))
    elif dig1 < dig2:
        print("{:02d}".format(i), end=", ")
