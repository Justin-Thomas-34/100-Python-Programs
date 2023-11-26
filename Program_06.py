# Program 06 : Python program to swap two variables

# Two methods to solve this problem
# 1) By using third temp variable
# 2) Without using temp variable

# Method 1: By using third temp variable

a = 20
b = 30
print("Before swapping:")
print("a:",a)
print("b:",b)

temp = a
a = b
b = temp

print("After swapping:")
print("a:",a)
print("b:",b)


# Method 2: Without using temp variable
x = 20
y = 40
print("Before swapping:")
print("x:",x)
print("y:",y)

x,y = y,x

print("After swapping:")
print("x:",x)
print("y:",y)