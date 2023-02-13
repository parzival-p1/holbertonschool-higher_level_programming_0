#!/usr/bin/python3
def safe_print_division(a, b):
    """ divides 2 integers and prints the result """
    try:
        div = a / b
        print("Inside Result: {:.1f}".format(div))
    except ZeroDivisionError:
        div = None
        print("Inside Result: {}".format(div))
    finally:
        return div
