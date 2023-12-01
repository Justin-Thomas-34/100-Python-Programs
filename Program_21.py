# Program 21: Python Program to find sum of n Natural Numbers

# Solution
num = int(input("Enter a number: "))

if num < 0:
    print("Please enter positive number")
else :
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print("Sum is", sum)