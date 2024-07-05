# Define a function to calculate the average grade of a student
def avgGrade(studentName):
    # Number of assignments (assuming it's constant for all students)
    # Initialize sum to accumulate grades
    currentAssignments = 5  
    sum = 0  
    
    for grade in studentName:
        # Add each grade in the studentName list to the sum
        sum += grade 

    # Calculate average grade
    avgGrade = sum / currentAssignments  
    return avgGrade

# Define lists of grades for each student
sophia = [93, 87, 98, 95, 100]
nicolas = [80, 83, 82, 88, 85]
zahirah = [84, 96, 73, 85, 79]
jeong = [90, 92, 98, 100, 97]

# Print header for the output
print("Student\t\t", "Grade")

# Print each student's name and their average grade using the avgGrade function
print("Sophia\t\t", avgGrade(sophia))
print("Nicholas\t", avgGrade(nicolas))
print("Zahirah\t\t", avgGrade(zahirah))
print("Jeong\t\t", avgGrade(jeong))
