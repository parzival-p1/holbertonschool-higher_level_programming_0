#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mult, div
    a = 10
    b = 5
    def add(a,b):
        return a + b
    def sub(a, b):
        return a - b	    
    def mul(a, b):
        return a * b
    def div(a, b):
        return a / b
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} + {} = {}".format(a, b, sub(a, b)))
    print("{} + {} = {}".format(a, b, mul(a, b)))
    print("{} + {} = {}".format(a, b, div(a, b)))
