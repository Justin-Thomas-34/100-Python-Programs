# Program 05: Python Program to Solve Quadratic Equation

# Quadratic Equation : ax**2 + bx + c = 0
# a,b,c are real number and a != 0
# Formula for discriminant 
# d = (b**2)-4ac
# Formula for root
# root1 = (-b - squareroot(b**2 - 4ac))/(2a)
# root2 = (-b + squareroot(b**2 - 4ac))/(2a)

# Solution :

import cmath            #importing cmath module
a = int(input("Enter a value for a which is not 0: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))

d = (b**2) - (4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print("The roots are", root1 , "and" , root2)


