#  Program 33 : Python Program to Find Factorial of Number using Recursion

# Solution:

def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))

n = int(input("Enter a number: "))

if n < 1:
    print("Factorial of number less than 1 does not exist")
else:
    print("Factorial of given number is",fact(n))

