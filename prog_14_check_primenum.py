'''This program checks whether the number is prime or not'''
import math

# Step 1: Handle user input and ensure it's an integer
try:
    num = int(input("Enter a positive integer: "))
except ValueError:
    print("Invalid Input! Please enter a whole number.")
    num = -1 # Set to negative to trigger the 'Invalid' check below

# Step 2: Filter out numbers less than 2 (not prime by definition)
if num < 0:
    print("Invalid Number! Please enter a positive integer.")
elif num <= 1:
    print(f"{num} is not a prime number.")
elif num == 2:
    print(f"{num} is a prime number.")
elif num % 2 == 0:
    # Any even number greater than 2 is not prime
    print(f"{num} is not a prime number.")
else:
    # Step 3: Optimization - Check only odd divisors up to the square root
    # Time Complexity: O(sqrt(n)), Space Complexity: O(1)
    is_prime = True
    limit = int(math.sqrt(num))
    
    for i in range(3, limit + 1, 2):
        if num % i == 0:
            is_prime = False
            break
            
    # Step 4: Final Output based on the flag
    if is_prime:
        print(f"{num} is a prime number!")
    else:
        print(f"{num} is not a prime number!")