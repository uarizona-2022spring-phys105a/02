#!/usr/bin/env python3
#
# 0. INTRODUCTION
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
# outline of the script already.
#
# For most part, you just need to follow the instruction to uncomment
# codes.  And even for the places that you need to program, all you
# need is some basic statements that we covered in the hands-on
# section:
#
#    https://github.com/uarizona-2022spring-phys105a/phys105a/blob/main/03/Handson.ipynb
#
# Please look for "TODO:" for the places that you are supposed to make
# change.
#
# Note, however, in order to explain how this script works, we need to
# jump to different parts of the code non-linearly.  To make it easier
# to find the code, we use a long line of `#====...====` to indicate
# these different "code sections".
#
# By the way, in interpreted language, there's no real difference
# between `program` and `script`.  So we will use these two terms
# interchangeablely in this file.
#
# To start, let's go to THE END of this script and look for
# "1. MAIN SECTION".
#
#==============================================================================
# 2. QUADRATIC EQUATION SOLVER
#
# NOTE: please read section "1. MAIN SECTION" before you read this section.
#
# Here, we want to program a function that solve the quadratic
# equation using the quadratic formula.  To demonstrate the traps in
# numerical analysis and computational science, we want to create
# multiple versions that we can compare with.

# import the square-root function from the standard math library
from math import sqrt

# The zeroth version is a straightforward implementation of the
# quadratic formula.
def quadratic0(a, b, c):
    x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    return (x1, x2)

# Make sure that you've uncommented the last two lines in the "1. MAIN
# SECTION".  And run
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
# This is a linear equation x + 2 == 0 and we human beings know the
# solution is simply -2.  However, computers are stupid and they only
# do exactly what you tell them to do.  quadratic0() does not know
# anything about linear equation, and it simply throw an
# ZeroDivisionError exception when it tries to follow the quadratic
# formula.
#
# To avoid this problem, let's develop an improved version of the
# quadratic formula.  We may even reuse the old quadratic0() function:
#
# TODO: fill in the correct condition in the following function, and
# update the second last line in the "1. MAIN SECTION" to use
# quadratic1() instead of quadratic0().
#
# Try
#
#    ./quadratic.py 0 1 2
#
# again and it should now be able handle this special case.
def quadratic1(a, b, c):
    if ______:
        return (-c / b,)
    else:
        return quadratic0(a, b, c)

# DISCUSSION:
#
# In principle, `b` and `c` may also be set to zero.  What should we
# do when that happen?  This won't be graded.  But we will discuss
# this in lecture 4 if there is time.

#------------------------------------------------------------------------------
# Try another case
#
#    ./quadratic.py 1 2 2
#
# This is a situation that the quadratic equation does not have a real
# root.  In quadratic0(), we simply take the square root of the
# discriminant = b**2 - 4 * a * c without checking its sign.  So let's
# improve our function again to handle it.
#
# TODO: fill in the correct conditions in the following function, and
# update the second last line in the "1. MAIN SECTION" to use
# quadratic2() instead of quadratic1().
#
# Try
#
#    ./quadratic.py 1 2 2
#
# again and it should now be able handle this case.
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

#------------------------------------------------------------------------------
# If computers can compute at infinite accuracy, then we are (almost)
# done!  But unfortunately, even if we use double precision float, the
# accuracy is only ~ 1e-16.  This may cause numerical problems even
# when we want to solve the simple quadratic formula!
#
# Let's consider the problem
#
#     (x + 1e8) * (x + 1e-8) == 0
#
# it has two roots at -1e8 and -1e-8, and expanse to
#
#     x^2 + 100000000.00000001 x + 1 == 0
#
# In fact, we expect the solutions to
#
#     x^2 + 1e8 x + 1 == 0
#
# to be very close to -1e8 and -1e-8.  Let use this to test out our algorithm:
#
#     ./quadratic.py 1 100000000.00000001 1
#     ./quadratic.py 1 1e8 1
#
# The less negative solutions are -1.49e-08 and -7.45e9, respectively,
# which are nearly 50% and 25% error.  This is UNACCEPTABLE, given
# that we expect the accuracy of double precision is ~ 1e-16.
#
# So what went wrong?  Looking at the quadratic formula, because `b`
# is positive, line 135
#
#     x1 = (-b + d) / (2 * a)
#
# subtracts two large numbers:
#
#     -1e8 + sqrt(1e16 - 1)
#
# So even the relative error is 1e-16, this can be a significant
# difference in the overall value of x1.
#
# This is one example that if we are not careful about our algorithm,
# it is possible to obtain garbage solution that is much worse than
# the numerical accuracy is able to perform.
#
# This is one form of NUMERICAL INSTABILITY.
#
# To avoid this problem, we need to improve our quadratic formula
# again to use numerically stable algorithm.  For this particular
# case, we simply need to avoid subtraction between two nearby
# numbers.
#
# Note that the solution of a quadratic equation satisfy
#
#     x1 x2 == c / a
#
# we can always replace a solution by:
#
#     x1 = (-b + d) / (2 * a) = c / (a x2) = (2 * c) / (-b - d)
#
# TODO: fill in the correct conditions in the following function, and
# update the second last line in the "1. MAIN SECTION" to use
# quadratic3() instead of quadratic2().
#
# Try
#
#     ./quadratic.py 1 100000000.00000001 1
#     ./quadratic.py 1 1e8 1
#
# again and it should give you the solutions -1e8 and -1e-8, which
# have numerical errors of order ~ 1e-16 instead of the terrible 50%
# and 25%!
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

# DISCUSSION:
#
# There is another place in quadratic3() where we need to compute the
# difference between two potentially nearby numbers.  Where is it?  Is
# there a strategy to provide numerically stable solution?

#==============================================================================
# 3. CONCLUSION
#
# This assignment walks you through the implementation of a script
# that solves for the quadratic equation.
#
# You should have learned
#
# a) how to structure a python script so it can be used as a command
#    line program.
#
# b) how to use functions
#
# c) how to use the if-else statement to take care different
#    conditions.
#
# d) how bad things can happen in computing with finite precision, and
#    how to resolve the "subtracting nearby numbers" problem by
#    reformulate equations to additions.
#
#==============================================================================
# 1. MAIN SECTION
#
# In software engineering, it is useful to break a program into
# multiple smaller functions so you can test each function
# independently.  In such a case, you will need a "driver script" that
# process the command line argument and pass them to the different
# functions.  We will do exactly this in this main section.

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

# Actually parse the command line arguments.
args = parser.parse_args()

# You can test the effect of the above line by typing:
#
#     ./quadratic.py
#
# in your command line.  It will tell you the program requires three
# arguments `a`, `b`, and `c`.  You may type
#
#     ./quadratic.py -h
#
# to see the help page and find out the meanings of `a`, `b`, and `c`.
# Note that, the above line would terminate this program if you don't
# give it three arguments.  So nothing below would be executed.

#------------------------------------------------------------------------------
# Now, assume you paid attention to the command line and typed in
# three arguments:
#
#    ./quadratic.py 1 2 1
#
# Let's print out the quadratic equation to tell the user that what
# this program is solving.
#
# Let's first assign the command line arguments back to variables
a = args.a
b = args.b
c = args.c

print("Solving the quadratic equation:", a, "x^2 +", b, "x +", c, "== 0")

# However, this script cannot solve anything yet.  To start
# programming a quadratic equation solver, you need to
#
# TODO: uncomment the following lines
#
# and then jump to the section "2. QUADRATIC EQUATION SOLVER"
#sol = quadratic0(a, b, c)
#print("Solutions", sol)
