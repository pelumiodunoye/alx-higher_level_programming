#!/usr/bin/python3

if _name_ = "_main":
    import sys
        count = len(sys.argv) - 1
        if count == 0:
            print("o arguments.")
        elif count == 1:
            print("1 arguments.")
        else:
            print("{} arguments.".format(count))
            for i in range(count):
                print("{}: {}".format(i +  1, sys.argv[i +  1]))
