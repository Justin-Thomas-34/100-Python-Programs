# Program 18 : Python Program to print the Fibonacci sequence

# Fibonacci sequence : 0,1,1,2,3,5,8,13,....  (sequence obtained by adding preceding 2 numbers)

# Solution
num = int(input("Enter the number to obtain fibonacci sequence: "))
a = 0
b = 1
if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,num):
        c = a + b
        a = b
        b = c
        print(c)
