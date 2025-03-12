

def right_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)
n = int(input("Enter number of rows: "))
right_triangle(n)


def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("*" * i)


n = int(input("Enter number of rows: "))
inverted_triangle(n)



def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
n = int(input("Enter number of rows: "))

