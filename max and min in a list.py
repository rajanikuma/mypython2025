def find_max_min(my_list):
    largest = max(my_list)  
    smallest = min(my_list)  
    return largest, smallest  
numbers = [10, 20, 4, 45, 99, 1]
largest, smallest = find_max_min(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)

