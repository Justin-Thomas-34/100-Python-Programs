# Program 48: Python Program to Iterate Over Dictionaries unif for loop

# Solution:

friends = {"Rachel":"Ross","Monica":"Cahndler","Phoebe":"Joe"}
print(friends)

# 1 using .items

for key,value in friends.items():
    print(key,"-",value)

# 2 using keys
for key in friends:
    print(key,":",friends[key])

# 3 using keys and values

for i in friends.keys():
    print(i)

for j in friends.values():
    print(j)
    

