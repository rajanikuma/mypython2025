

def is_palindrome(value):
    value = str(value)  
    return value == value[::-1]
user_input = input("Enter a number or string: ")

if is_palindrome(user_input):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
print(" Rajani 60")
