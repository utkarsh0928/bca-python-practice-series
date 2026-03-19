'''This program used to calculate the logarithmic of two numbers.'''
import math
def main():
    '''This function used to calculate the logarithmic of two numbers.'''
    num1 = float(input("Enter the first number: ")) # The first number is the number for which we want to calculate the logarithm.
    num2 = float(input("Enter the second number: ")) # The second number is the base of the logarithm. It must be greater than 1 and not equal to 1.
    log_result = round(math.log(num1, num2), 2)
    print(f"The logarithm of {num1} to the base {num2} is: {log_result}")
main()