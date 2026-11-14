
# Create a list of tracked subjects
subjects = ["Math", "Science", "English"]


# Function to collect and validate student information
def add_student(student_number, subjects):

    # Get student name
    while True:  # Repeat until name is entered
        # Prompt for student name, strip surrounding whitespace
        name = input(f"Enter name of student {student_number}: ").strip()

        # If name var is not empty, break loop
        if name:
            break

        # Print error if name is left empty
        print("Student name cannot be empty.")

    # Initialize list to store grades input
    grades = []

    # Iterate over each subject to collect grades
    for subject in subjects:

        # Validate grade input.
        while True:  # Repeat until valid grade is entered
            try:
                # Prompt for grade, convert to float
                grade = float(input(f"Enter grade for {subject}: "))

                # Check that grade is within allowed range
                if 0 <= grade <= 100:
                    # Exit loop if grade is valid
                    break

                # Notify user that grade is invalid
                print("Grade must be between 0 and 100.")

            # Handle input that cannot be converted to float
            except ValueError:
                # Notify user that input is invalid
                print("Invalid input. Please enter numeric grade.")

        # Append grade to 'grades' list
        grades.append(grade)

    # Return student info as tuple
    return (name, grades)


# Function to calculate each student's average
def calculate_averages(students):

    # Create list to store student averages
    averages = []

    # Iterate over each student and retrieve name and grades
    for name, grades in students:

        # Calculate average by dividing total points by number of subjects
        average = sum(grades) / len(grades)

        # Append averages to list
        averages.append(average)

    # Return list of student averages
    return averages


# Function to format and display the student report
def format_report(students, subjects, averages):

    # Create header for final grades display
    print("=" * 40)
    print(f"{'STUDENT GRADES':^40}")
    print("=" * 40)
    print()

    # Iterate over each student and their calculated average
    for (name, grades), average in zip(students, averages):

        # Print student name
        print(f"Student: {name}")

        # Iterate through subjeccts and grades, print into aligned columns
        for subject, grade in zip(subjects, grades):
            print(f"{subject + ':':<20} {grade:>10.2f}")

        # Print grade average into aligned column
        print(f"{'Average Grade:':<20} {average:>10.2f}")
        print()

# Function to display data type and identity of studen tuple
def variable_info(students):

    # Display the data type of the student tuple
    print(f"\nStudent Data Type: {type(students)}")

    # Display the identity of the student tuple
    print(f"Student Data ID: {id(students)}")

# Main program

# Create program header
print("=" * 40)
print(f"{'GRADEBOOK':^40}")
print("=" * 40)
print()

# Create empty list for student information
student_records = []

# Iterate twice to collect infor for two students
for student in range(2):

    # Collect student info and append it to records list
    student_records.append(add_student(student + 1, subjects))
    print()

# Convert student info into outer tuple
    students = tuple(student_records)

# Calculate averages for each students
averages = calculate_averages(students)

# Display formatted student report
format_report(students, subjects, averages)

# Display student data type and identity
variable_info(students)

