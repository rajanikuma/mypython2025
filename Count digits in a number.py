
def count_digits(number):
    return len(str(abs(number)))  
try:
    num = int(input("Enter an integer: "))
    digit_count = count_digits(num)
    print(f"Number of digits: {digit_count}")
except ValueError:
    print("Invalid input! Please enter an integer.")

print ("RAJANI 60")
