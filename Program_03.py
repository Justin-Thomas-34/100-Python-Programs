# Program to find the square root

#  There are two methods to solve this problem
# 1) Using exponatiation operator
# 2) Using math module

# Solution 1: Using exponatiation operator

    # Predefined number  

num1 = 64
sr1 = num1 ** (1/2)  
print("The squareroot of number is", sr1 )



    # User input number

num2 = int(input("Enter a number: "))
sr2 = num2 ** (0.5)  # because 1/2 is equal to 0.5
print("The squareroot of number is", sr2)


# Solution 2: Using math module

    # Predefined number  
    
import math  # importing math module
num3 = 64
sr3 = math.sqrt(num3)  
print("The squareroot of number is", sr3 )



    # User input number
    
num4 = int(input("Enter a number: "))
sr4 = math.sqrt(num4) 
print("The squareroot of number is", sr4)