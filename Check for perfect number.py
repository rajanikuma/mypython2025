

def is_perfect_number(n):
    if n < 1:
        return False  
    
    divisors_sum = sum(i for i in range(1, n) if n % i == 0) 
    
    return divisors_sum == n
num = int(input("Enter an integer: "))
if is_perfect_number(num):
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")
    print(" Rajani 60")
