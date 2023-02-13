#!/usr/bin/python3
def safe_print_division(a, b):
    """ divides 2 integers and prints the result """
    div = None
    try:
        div = a / b
    except ZeroDivisionError:
        return div
    finally:
        print("Inside Result: {}".format(div))
    return div
