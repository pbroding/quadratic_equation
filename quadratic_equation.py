"""Quadratic equation formula program. Need values for a, b, and c variables to produce
    two values for x. Will use a while loop, with us seperate functions for each x value. 
    Will also use a try/except block to deal with imaginary numbers."""

import math
import cmath

def first_x(a,b,c):
    """This function produces the first x value for the quadratic equation."""
    z = ((b**2)-(4*a*c))
    try:
        y = math.sqrt(z)
    except ValueError:
        y = cmath.sqrt(z)
    x = ((-b) + (y))/(2*a)
    return x
def second_x(a,b,c):
    """This function produces the second x value for the quadratic equation."""
    z = ((b**2)-(4*a*c))
    try:
        y = math.sqrt(z)
    except ValueError:
        y = cmath.sqrt(z)
    x = ((-b) - (y))/(2*a)
    return x

print("This is a quadratic equation program, which is based off the quadratic formula.")
print("All you need to do is provide the values for a, b, and c and it will return two values for x.")
print("Press 'q' for any value to quit.")

while True:
    a = input("Enter the value for a: ")
    if a == 'q':
        break
    else:
        a = int(a)
    b = input("Enter the value for b: ")
    if b == 'q':
        break
    else:
        b = int(b)
    c = input("Enter the value for c: ")
    if c == 'q':
        break
    else:
        c = int(c)
    first_solution = first_x(a,b,c)
    second_solution = second_x(a,b,c)
    print(f"First solution: {first_solution}")
    print(f"Second solution: {second_solution}")
    quit = input("Press 'q' to quit or press 'Enter' to continue program: ")
    if quit == 'q':
        break
