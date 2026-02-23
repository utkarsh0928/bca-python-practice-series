'''This program is used to swap two variables without temp variable'''
a=float(input("Enter number a:"))
b=float(input("Enter number b:"))
print(f"Number before swapping; a:{a},b:{b}")
#Swapping variables using tuple unpacking
a,b=b,a
print(f"Number after swapping; a:{a},b:{b}")
