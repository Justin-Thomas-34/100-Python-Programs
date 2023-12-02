# Program 23: Python Program to Find Numbers Divisible by Another Number

# Solution:

# Method 1: using for loop and conditional statement

num1 = int(input("Enter a number: "))

print("The numbers divisible by", num1 , "are")

for i in range(1,100):
    if i%num1 == 0:
        print(i)



# Method 2: using lambda function and filter()

num2 = int(input("Enter a number: "))

l = list(range(1,100))
result = list(filter(lambda x : x%num2==0,l))

print("The numbers divisible by",num2,"are",result)