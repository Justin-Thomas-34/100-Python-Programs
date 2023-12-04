# Program 26: Python Program to Find HCF or GCD

# HCF - Highest Common Factor 
# GCD - Greatest Common Divisor 

# Solution


def findHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if (x%i == 0) and (y%i == 0):
            hcf = i
    return hcf


x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print("The HCF of given two numbers is: ",findHCF(x,y))