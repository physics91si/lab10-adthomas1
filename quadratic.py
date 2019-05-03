#!/usr/bin/python
import sys
import math
#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    try:
        x1, x2 = find_roots(int(a),int(b),int(c))
    except ValueError:
        print("Input must be Integers.")
        sys.exit(1)
    print ("This is x1: %f" %x1)
    print ("This is x2: %f" %x2)


def find_roots(a,b,c):
    mid = b*b - 4*a*c
    try:
        sqrt_mid = math.sqrt(mid)
    except ValueError:
        print("Cannot handle imaginary solutions.")
        sys.exit(1)
    try:
        x1 = (b + sqrt_mid)/(2*a)
        x2 = (-b - sqrt_mid)/(2*a)
    except ZeroDivisionError:
        print("The eqution must be quadratic, not linear.")
        sys.exit(1)
    return x1, x2

if __name__=="__main__":
        main()
