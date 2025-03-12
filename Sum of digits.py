

def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))  
try:
    num = int(input("Enter a number: "))
    digit_sum = sum_of_digits(num)
    print(f"Sum of digits: {digit_sum}")
except ValueError:
    print("Invalid input! Please enter an integer.")

print (" Rajani 60")
