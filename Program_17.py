# Program 17 : Python Program to Display Multiplication Table

# Solutiom

# Method 1: Using for loop

num1 = int(input("Enter a number: "))
for i in range(1,11):
    print(num1,"x",i,"=",num1*i)


# Method 2: using while loop

num2 = int(input("Enter a number: "))
j = 1
while j <= 10:
    print(num2,"x",j,"=",num2*j) 
    j += 1