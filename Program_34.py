# Program 34: Python program to Convert Decimal to Binary Using Recursion

# Solution: 

def ConvertBinary(n):
    if n > 1:
        ConvertBinary(n//2)
    print(n%2,end="")


print("The binary of given number is: ")
ConvertBinary(15)

