

import math

def math_operations(n):
    square_root = math.sqrt(n)
    factorial = math.factorial(n) if n >= 0 and n == int(n) else "Undefined for non-integers or negative numbers"
    sine_value = math.sin(math.radians(n))  

    print(f"Square Root of {n}: {square_root}")
    print(f"Factorial of {n}: {factorial}")
    print(f"Sine of {n} degrees: {sine_value}")

number = 5
math_operations(number)
print(" Rajani 60")
