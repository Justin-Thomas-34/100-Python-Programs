# Program 42: Python Program to Count the number of each vowel

# Solution:

# 1 Using Dictionary

a = "Harry Potter and the prisoner of Azkaban"

vowels = "aeiou"

a = a.casefold()
print(a)
count = {}.fromkeys(vowels,0)

for char in a:
    if char in count:
        count[char] += 1

print(count)

# 2. Using list and dictionary comprehension

b = "Harry Potter and the prisoner of Azkaban"

vowels = "aeiou"

b = b.casefold()

count = {key:sum([1 for char in a if char == key]) for key in vowels}
print(count)