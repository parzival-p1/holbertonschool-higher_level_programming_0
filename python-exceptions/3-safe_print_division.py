#!/usr/bin/python3
def safe_print_division(a, b):
    """ divides 2 integers and prints the result """
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
        return
    finally:
        print("Inside Result: {}".format(div))
        return div
