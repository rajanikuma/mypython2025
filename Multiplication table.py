

def multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

try:
    num = int(input("Enter an integer: "))
    multiplication_table(num)
except ValueError:
    print("Invalid input! Please enter an integer.")

print(" Rajani 60 ")
