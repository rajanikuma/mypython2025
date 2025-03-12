def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"


try:
    marks = float(input("Enter student's marks: "))
    if 0 <= marks <= 100:
        grade = get_grade(marks)
        print(f"Student's grade: {grade}")
    else:
        print("Please enter a valid mark between 0 and 100.")
except ValueError:
    print("Invalid input! Please enter a numeric value.")

print (" Rajani")
