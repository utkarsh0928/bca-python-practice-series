'''
This program takes two numbers as input from the user, divides them, and prints the result.
'''
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
if num2 != 0:
  divs=num1/num2
  print(f"The division of {num1} and {num2} is {divs}")
else:
  print("Error: Division by zero is not allowed.")