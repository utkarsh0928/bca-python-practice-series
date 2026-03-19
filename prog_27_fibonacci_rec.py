'''This program is used to generate fibonacci numbers using recursion.'''
def fibonacci(n):
    '''This function is used to generate fibonacci numbers using recursion.'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))