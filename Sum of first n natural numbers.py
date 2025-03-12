def sum_natural_numbers(N):
    return (N * (N + 1)) // 2
try:
    N = int(input("Enter a positive integer N: "))
    if N > 0:
        result = sum_natural_numbers(N)
        print(f"Sum of the first {N} natural numbers: {result}")
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input! Please enter a numeric value.")

print ( "Rajani 60")
