# Program 38: Python Program to Check Weather a String is Palindrome or Not

# Solution:

a = input("Enter a word: ")
rev = a[::-1]
if a == rev:
    print(a,"is a Palindrome")
else:
    print(a,"is not a Palindrome")