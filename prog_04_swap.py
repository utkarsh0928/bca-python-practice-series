'''
This program is doing swapping of two variables using temp variable
'''
var1=input("Enter the variable 1:")
var2=input("Enter the variable 2:")
print(f"Original Values: a={var1} , b={var2}")
temp=var1
var1=var2
var2=temp
print(f"Swapped Values: a={var1} , b={var2}")