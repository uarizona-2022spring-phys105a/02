#!/usr/bin/env python3

from math import sqrt

def quadratic0(a, b, c):
    x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    return (x1, x2)

def quadratic1(a, b, c):
    if ______:
        return (-c / b,)
    else:
        return quadratic0(a, b, c)

def quadratic2(a, b, c):
    if ______:
        return (-c / b,)
    else:
        D = b**2 - 4 * a * c
        if ______:
            d  = sqrt(D)
            x1 = (-b + d) / (2 * a)
            x2 = (-b - d) / (2 * a)
            return (x1, x2)
        else:
            return ()

def quadratic3(a, b, c):
    if ______:
        return (-c / b,)
    else:
        D = b**2 - 4 * a * c
        if ______:
            d = sqrt(D)
            if ______:
                x1 = (-b - d) / ( 2 * a)
                x2 = ( 2 * c) / (-b - d)
            else:
                x1 = (-b + d) / ( 2 * a)
                x2 = ( 2 * c) / (-b + d)
            return (x1, x2)
        else:
            return ()

import argparse

parser = argparse.ArgumentParser(description="""
This program takes exactly three arguments from the command line,
interpret those as the coefficients `a`, `b`, and `c` of a quadratic
equation, `a x^2 + b x + c == 0` and then return the roots according
to the quadratic formula `x = (-b +- sqrt(b^2 - 4 a c)) / (2 a)`.
""")
parser.add_argument('a', type=float, help='the coefficient of the quadratic term')
parser.add_argument('b', type=float, help='the coefficient of the linear    term')
parser.add_argument('c', type=float, help='the coefficient of the constant  term')
args = parser.parse_args()

a, b, c = args.a, args.b, args.c

print("Solving the quadratic equation:", a, "x^2 +", b, "x +", c, "== 0")
#sol = quadratic0(a, b, c)
#print("Solutions", sol)
