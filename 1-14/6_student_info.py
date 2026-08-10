# Program to find student name, marks, percentage and display grade

name = input("Enter student name: ")
marks = float(input("Enter marks: "))
percentage = float(input("Enter percentage: "))

# Validation
if percentage <= 0 or percentage > 100:
    print("Invalid percentage!")
else:
    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Percentage:", percentage)

    # Grade calculation
    if percentage >= 75:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 40:
        print("Grade: C")
    else:
        print("Grade: Fail")       