# Program 40: Python Program to Sort Words in Alphabetic Order

# Solution: 

a = input("Enter a sentence here: ")

w = a.split()
for i in range(len(w)):
    w[i] = w[i].lower()

w.sort()
for i in w:
    print(i)