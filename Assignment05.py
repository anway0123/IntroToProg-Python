# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Niki Way,02/25/2025, Created Script
# ------------------------------------------------------------------------------------------ #


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data:dict = {}  # one row of student data
students: list = []  # a table of student data
json_data = ''
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
import json
# Extract the data from the file
try:
    file = open("Enrollments.json", "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print('Text file must exist before running this script!]\n')
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data

    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            if not student_first_name.isalpha():
                raise Exception('The first name should not contain numbers.')
        except ValueError as e:
            print(e)
            print('---Technical Error Message---')
            print(e.__doc__)
            print(e.__str__())
            if not student_last_name.isalpha():
                raise Exception('The last name should not contain numbers.')
        except Exception as e:
            print(e)
            print('---Technical Error Message---')
            print(e.__doc__)
            print(e.__str__())
        course_name = input("Please enter the name of the course: ")
        student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in " + \
                  f"{student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open("Enrollments.json", "w")
            json.dump(students,file)
            file.close()
        except TypeError as e:
            print("Please check that the data is a vaild JSON format\n")
            print("--Technical Error Message --")
            print(e,e.__doc__,type(e),sep='\n')
        finally:
            if file.closed == False:
                file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
