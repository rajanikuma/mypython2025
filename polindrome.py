def is_polindrome(value):
    value = str(value)

    return value == value[::-1]

    word = input ("Enter a word or number:")
    if is_palindrome(word):
        print("it is a polindrome")
    else:
        print("it is not a polindrome")
