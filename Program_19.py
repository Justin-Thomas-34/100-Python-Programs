# Program 19: Python Program to Check Armstrong Number

# Armstrong Number 153 = 1*1*1 + 5*5*5 + 3*3*3 = 1 + 125 + 27 = 153 (the number in any given base , which forms the total of the same number  when each of its digits is raised to the power of the number of digits in the number)
# 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1 + 1296 + 81 + 256 = 1634

# Solution

num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp%10
    sum += digit**order
    temp //= 10

if sum == num:
    print(num," is a Armstrong Number")
else:
    print(num," is not a Armstrong Number")
