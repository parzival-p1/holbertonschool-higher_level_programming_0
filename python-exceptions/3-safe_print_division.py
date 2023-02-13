#!/usr/bin/python3
def safe_print_division(a, b):
    """ divides 2 integers and prints the result """
    div = 0 
    try:
        div = a / b
    except ZeroDivisionError:
        div = None 
    finally:
        print("Inside Result: {}".format(div))
        return div
