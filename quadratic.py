#!/usr/bin/env python3
#
# 0. Introduction
#
# This is the assignment for week 3 for PHYS 105A.
#
# In this assignment, you will write a python script that takes
# exactly three arguments from the command line, interpret those as
# the coefficients `a`, `b`, and `c` of a quadratic equation,
#
#     a x^2 + b x + c == 0
#
# and then return the roots according to the quadratic formula.
#
#     x = (-b +- sqrt(b^2 - 4 a c)) / (2 a)
#
# This may sound non-trivial if this is your first computer
# programming assignment.  But don't worry, we've provided you an
# outline of the script already.  For most part, you just need to
# follow the instruction to uncomment codes.  And even for the places
# that you need to program, all you need is the basic statements that
# we covered in the hands-on section:
#
#    https://github.com/uarizona-2022spring-phys105a/phys105a/blob/main/03/Handson.ipynb
#
# Please look for "TODO:" for the places that you are suppose to make
# change.
#
# Note, however, in order to explain how this script works, we need to
# jump to different part of the code non-linearly.  To make it easily
# to find the code, we use a long block of #====...==== to indicate
# these different "code sections".
#
# By the way, in interpreted language, there's no real difference
# between `program` and `script`.  So we will use these two terms
# interchangeablely in this file.
#
# To start, let's go to THE END of this script and look for the "1. MAIN BLOCK"
#
#==============================================================================
# 2. QUADRATIC EQUATION SOLVER
#
# NOTE: please read block "1. MAIN BLOCK" before you read this block.
#
# Here, we want to program a function that solve the quadratic
# equation using the quadratic formula.  To demostrate the traps in
# numerical analysis and computational scinece, we want to create
# multiple versions that we can compare with.

# import the square-root function from the standard math library
from math import sqrt

# The zeroth version is a straightforward implementation of the
# quadratic formula.
def quadratic0(a, b, c):
    x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    return (x1, x2)

# Make sure that've uncommented the last two lines in the "1. MAIN
# BLOCK".  And run
#
#    ./quadratic.py 1 2 1
#    ./quadratic.py 1 -2 1
#    ./quadratic.py 1 4 3
#    ./quadratic.py 1 -4 3
#
# Yeah!  The program seems to work.

#------------------------------------------------------------------------------
# Now, try the following case:
#
#    ./quadratic.py 0 1 2
#
# This is a linear equation x + 2 == 0 and we know the solutoin is
# simply -2.  However, quadratic0() simply throw an ZeroDivisionError
# exception.
#
# To avoid this problem, let's develop an improved version of the
# quadratic formula.  We may even reuse the old quadratic0() function:
#
# TODO: fill in the correct condition in the following function, and
# update the second last line to use quadratic1() instead of
# quadratic0().
def quadratic1(a, b, c):
    if ________:
        return (-c / b,)
    else:
        return quadratic0(a, b, c)

#==============================================================================
# 1. MAIN BLOCK
#
# In software engineering, it is useful to break a program into
# multiple smaller functions so you can test each function
# independently.  In such a case, you will need a "driver script" that
# process the command line argument and pass them to the different
# functions.  We will do exactly this in this main block.

# Import the standard `argparse` package to help us process command
# line input.
import argparse

# Documentation is very important in programming.  So let's provide a
# short description of this program, which I simply copied from the
# comment at the beginning of this script.
parser = argparse.ArgumentParser(description="""
This program takes exactly three arguments from the command line,
interpret those as the coefficients `a`, `b`, and `c` of a quadratic
equation, `a x^2 + b x + c == 0` and then return the roots according
to the quadratic formula `x = (-b +- sqrt(b^2 - 4 a c)) / (2 a)`.
""")

# We want this program to take exactly 3 arguments.
parser.add_argument('a', type=float, help='the coefficient of the quadratic term')
parser.add_argument('b', type=float, help='the coefficient of the linear    term')
parser.add_argument('c', type=float, help='the coefficient of the constant  term')

# Actually parse the command line arguments.  You can test the effect
# of this line by typing:
#
#     ./quadratic.py
#
# in your command line.  It will tell you the program requires three
# arguments `a`, `b`, and `c`.  You may type
#
#     ./quadratic.py -h
#
# to see the help page and find out the meanings of `a`, `b`, and `c`.
# Note that, the following line would terminate this program if you
# don't give it three arguments.  So nothing below the following line
# would be executed.
args = parser.parse_args()

#------------------------------------------------------------------------------
# Now, assume you paid attention to the command line and typed in
# three arguments:
#
#    ./quadratic.py 1 2 1
#
# Let's print out the quadratic equation to tell the user that what
# this program is sovling.
#
# Let's first assign the command line arguments back to variables
a = args.a
b = args.b
c = args.c

print("Sovling the quadratic equation:", a, "x^2 +", b, "x +", c, "== 0")

# However, this script cannot solve anything yet.  To start
# programming a quadratic equation solver, you need to
#
# TODO: uncomment the following lines
#
# and then jump to the block "2. QUADRATIC EQUATION SOLVER"
#sol = quadratic0(a, b, c)
#print("Solutions", sol)
