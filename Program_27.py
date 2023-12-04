# Program 27 : Python Program to Find Facors of a number

# Solution

num =int(input("Enter a number:  "))

for i in range (1,num+1):
    if num%i == 0:
        print(i)