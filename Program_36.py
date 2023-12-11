# Program 36: Python program to Transpose a Matrix

# Solution:

#1. Using for loop

A = [[1,2,3],
     [4,5,6]]

T = [[0,0],
     [0,0],
     [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i] = A[i][j]

for k in T:
    print(k)

#2. Using list comprehension

B = [[1,2,3],
     [4,5,6]]

T1 = [[B[l][m] for l in range(len(B))] for m in range (len(B[0]))]

for m in T1:
    print(m)