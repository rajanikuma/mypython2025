def count_occurrences(my_list, element):
    return my_list.count(element)  
numbers = [10, 20, 10, 4, 10, 45, 99]
element_to_count = 10
count = count_occurrences(numbers, element_to_count)
print(f"The element {element_to_count} appears {count} times in the list.")
