# Program 15: Python Program to print all Prime Numbers is an Interval

# Solution

lower = int(input("Enter a lower limit of range: "))
upper = int(input("Enter a upper limit of range: "))

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)
