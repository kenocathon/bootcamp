### import math for sqrt
from math import sqrt
print('Enter your coefficients and I will try to solve the quadratic equation')

def quad():
    #create while loop that verifies root is a digit
    keepgoing = True
    while keepgoing:
        a = float(input('Enter the number for a: '))
        b = float(input('Enter the number for b: '))
        c = float(input('Enter the number for c: '))
        # calculate inside sqrt
        in_root = b ** 2 - 4 * a * c
        #validate in_root
        if in_root > 0:
            #take sqrt of in_root
            d = sqrt(in_root)
            # add and subtract equations
            add = (-b + d) / (2 * a)
            subtract = (-b - d) / (2 * a)
            #print solution
            print('Your solutions are')
            print('x = {0}'.format(add))
            print('x = {0}'.format(subtract))
            keepgoing = False

        else:
            print('This is an imaginary number make sure numbers\ninside sqrt evaluate to a positive number')

quad()
        