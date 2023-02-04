"""
Author:  Param Patel

Language:  Python 3

Purpose: This file has two methods that converts the F to C and C to F.

Bugs: None so far. But if you find any bugs let me know! :-)
"""


def c_to_f(number):
    C = (number * 9 / 5) + 32
    return C


def f_to_c(number):
    F = (number - 32) * 5 / 9
    return F
