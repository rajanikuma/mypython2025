import math

def lcm(num1, num2):
    return abs(num1 * num2) // math.gcd(num1, num2)

result = lcm(30,55)
print(result)  
