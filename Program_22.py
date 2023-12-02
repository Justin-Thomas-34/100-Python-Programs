# Program 22 : Python Program to display Powers of 2 Using Anonymous Function(Lambda Function)

# Solution:
 
nterms = int(input("Enter number of terms: "))

result = list(map(lambda x : 2**x,range(nterms+1)))

for i in range(nterms+1):
    print("The value of 2 raised to power",i,"is",result[i])