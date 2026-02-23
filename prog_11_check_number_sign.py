'''This program is check the number whether it is zero, negative or positive'''
num=float(input("Enter the number:"))
# Conditional logic to check the sign
if num<0:
    print("Negative")
elif num>0:
    print("Positive")
else:
    print("Zero")