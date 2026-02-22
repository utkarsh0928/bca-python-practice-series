'''
This program is used to solve the problem of quadratic with using the math library 
'''
import math

# User input: Convert strings to floats for numerical calculation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant (d = b^2 - 4ac)
# This value determines the nature of the roots
discriminant = b**2 - 4*a*c

# Case 1: Two distinct real roots
if discriminant > 0:
    # Applying the quadratic formula: (-b ± sqrt(d)) / 2a
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two real roots: {root1} and {root2}")

# Case 2: One repeated real root (Discriminant is zero)
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One repeated real root: {root}")

# Case 3: Complex roots (Discriminant is negative)
else:
    # The real part is -b / 2a
    real_part = -b / (2*a)
    # The imaginary part uses the square root of the absolute value of the discriminant
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Complex Roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")