#  Program 28 : Python Program to Make a Simple Calculator

#  Solution:
print("~~~~~~~~MINI CALCULATOR~~~~~~~~~~")
 
num1 = float(input("Enter a number: "))
num2 = float(input("Enter second number: "))
print("Press 1 for Addition \n Press 2 for Subtraction \n Press 3 for Multiplication \n Press 4 for Division ")
choice = int(input("Enter your choice from 1 - 4: "))

if choice == 1:
    print("The Adition of given two numbers is: ",num1 + num2)
elif choice == 2:
    print("The Subtraction of given two numbers is: ",num1 - num2)
elif choice == 3:
    print("The Multiplication of given two numbers is: ",num1 * num2)
elif choice == 4:
    print("The Division of given two numbers is: ",num1 / num2)    
else:
    print("Invalid Input")