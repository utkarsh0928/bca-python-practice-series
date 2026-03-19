'''This program is used as a simple calculator for the user. It can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The user can input two numbers and select the desired operation to get the result.'''

def add(x, y):
    '''This function adds two numbers and returns the result.'''
    return x + y
def subtract(x, y):
    '''This function subtracts the second number from the first number and returns the result.'''
    return x - y
def multiply(x, y):
    '''This function multiplies two numbers and returns the result.'''
    return x * y
def divide(x, y):
    '''This function divides the first number by the second number and returns the result. It also checks for division by zero.'''
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
def main():
    '''This is the main function that runs the calculator program. It prompts the user for input and performs the selected operation.'''
    print("Welcome to the simple calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    print("Thank you for using the simple calculator! Goodbye!")

if __name__ == "__main__":
    main()