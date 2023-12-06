# Program 31: Python Program to Display Fibonacci Sequence Using Recursion

# Solution:
 
def fibo(n):

    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter a number here: "))

if n <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci Sequence")
    for i in range(n):
        print(fibo(i))
