'''This program is used to calculate the factorial of a number using recursion.'''
def factorial(n):
    '''This function calculates the factorial of a number using recursion.'''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
if __name__ == '__main__':
    number = int(input('Enter a number to calculate its factorial: '))
    print(f'The factorial of {number} is {factorial(number)}')