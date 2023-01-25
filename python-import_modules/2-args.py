#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    print("{} {}{}".format(l - 1, "argument" if l <= 2 else "arguments",
                           "." if l == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{}: {}".format(i, s))
