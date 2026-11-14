
# Get name of first student
student_1 = input("Enter name of first student: ")

# Get english grade for first student
english_1 = float(input("Enter english grade: "))

# Get math grade for first student
math_1 = float(input("Enter math grade: "))

# Get english grade for first student
science_1 = float(input("Enter science grade: "))

# Store grades for first student in list
student_1_grades = [english_1, math_1, science_1]

print()    # print blank line

# Get name of student 2
student_2 = input("Enter name of second student: ")

# Get english grade for second student
english_2 = float(input("Enter english grade: "))

# Get math grade for second student
math_2 = float(input("Enter math grade: "))

# Get english grade for second student
science_2 = float(input("Enter science grade: "))

# Store grades for second student in list
student_2_grades = [english_2, math_2, science_2]


# Create tuple containing student names and student grade lists
students = (
    (student_1, student_1_grades),
    (student_2, student_2_grades)
)

# calculate student 1's average
student_1_average = sum(student_1_grades) / 3

# calculate student 2's average
student_2_average = sum(student_2_grades) / 3

# Print student 1's name and average to 2 decimal places
print()
print(f"Student Name: {student_1}")
print(f"Student grade average: {student_1_average:.2f}")

# Print student 2's name and average to 2 decimal places
print()
print(f"Student Name: {student_2}")
print(f"Student grade average: {student_2_average:.2f}")

# Print type and id for 'students' tuple
print()
print(
    f"Object: 'students', 'Type:' {type(students)}, 'ID:' {id(students)}"
)

# print type and id for 'student_1_grades' list
print()
print(
    f"Object: 'student_1_grades', "
    f"Type: {type(student_1_grades)}, "
    f"ID: {id(student_1_grades)}"
      )

# print type and id for 'student_2_grades' list
print()
print(
    f"Object: 'student_2_grades', "
    f"Type: {type(student_2_grades)}, "
    f"ID: {id(student_2_grades)}"
)
