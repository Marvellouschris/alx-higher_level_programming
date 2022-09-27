#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    rev = reversed(my_list)
    for int in rev:
        print("{:d}".format(int))
