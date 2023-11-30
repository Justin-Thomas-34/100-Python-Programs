# Program 16: Python Program to find Factorial of a number

#  Factorial : 5! = 5*4*3*2*1
# number < 0 no factorial
# number = 0 factorial = 1
# number > 0 factorial exists

# Solution

# Method 1 : Using for loop

num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("Factorial of negative number does not exists. ")
elif num == 0:
    print("Factorial of",num,"= ",1)
elif num > 0:
    for i in range(1,num+1):
        fact = fact * i
    print("Factorial of ",num,"=",fact)


# Method 2 : Using recursion
def factorial(a):
    if a == 0:
        return 1
    else:
        return ((a)*factorial(a-1))
    
num1 = int(input("Enter a number: "))

result = factorial(num1)
print("The factorial of",num1,"=",result)