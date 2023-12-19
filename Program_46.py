# Program 46: Python Program to Access Index of a List Using for Loop

# Solution:

# 1 using enumerate method

l = [34,5,61,54,89]
for index, value in enumerate(l):
    print(index,"-",value)

# 2 not using enumerate method

l = [34,5,61,54,89]
for index in range(len(l)):
    value = l[index]
    print(index,"-",value)
