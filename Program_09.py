# Python Program to convert Celsius to Fahrenheit

# Formula: 0 Celsius = 32 Fahrenheit 
# Fahrenheit = (Celsius * (9/5)) + 32


celsius = int(input("Enter temperature in celsius:"))
fahrenheit = (celsius * (9/5))+32
print("The converted value is ", fahrenheit ,"fahrenheit")



# Python Program to convert Fahrenheit to Celsius

# Formula: 0 Celsius = 32 Fahrenheit 
# Celsius  = (Fahrenheit - 32)*(5/9)  


f = int(input("Enter temperature in fahrenheit:"))
c = (f-32)*(5/9)
print("The converted value is ", c ,"celsius")