# Program 12: Python Program to Check Leap Year

# if a year is divisible by 4  and not divisible by 100 it is leap year. if a centuary year is divisible by 400 and 100 it is a leap year.

# Solution

year = int(input("Enter a year: "))

if (year%4 == 0) and (year%100 != 0):
    print(year," is a leap year")
elif (year%100 == 0) and (year%400 == 0):
    print(year," is a leap year")
else:
    print(year, "is not a leap year")