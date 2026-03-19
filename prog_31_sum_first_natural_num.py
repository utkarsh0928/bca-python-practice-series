'''This program is used to calculate the sum of first n natural numbers.'''
def main():
    '''This function is used to calculate the sum of first n natural numbers.'''
    n = int(input("Enter a positive integer: "))
    if n < 1:
        print("Please enter a positive integer.")
        return
    sum_natural = n * (n + 1) // 2
    print(f"The sum of the first {n} natural numbers is: {sum_natural}")
main()