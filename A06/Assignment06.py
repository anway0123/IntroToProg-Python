# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#  Niki Way, 3/5/2025, Created Script
# ------------------------------------------------------------------------------------------ #


# Processing --------------------------------------- #
import json

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
FILE_NAME_CSV: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []
menu_choice: str

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    NWay,3.4.2025,Created Class
    """
    pass

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads data from file and convert it into a list of dictionaries

        ChangeLog: (Who, When, What)
        NWay,3.4.2025,Created function
        :param file_name: file that is being read from
        :param student_data: list of dictionary rows
        :return: list of dictionaries
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!",e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!",e)
        finally:
            if file.closed == False:
                file.close()
            return student_data

    @staticmethod
    def write_data_to_file(file_name: str, file_name_csv: str, student_data: list):
        # global file
        # global students
        """ This function writes data to a json file with data from a list of dictionary rows
        ChangeLog: (Who, When, What)
        NWay,3.4.2025,Created function
        :param file_name: JSON file that is being written in
        :param file_name_csv: CSV file that is being written in
        :param student_data: list of dictionary rows
        :return: None
        """
        try:

            # JSON
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()

            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')

            # CSV
            file = open(file_name_csv, "w")
            for student in students:
                csv_data = f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n'
                file.write(csv_data)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON or CSV format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    NWay,3.4.2025,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error messages to the user
        ChangeLog: (Who, When, What)
        NWay,3.4.2025,Created function
        :param message: string with message for user display
        :param error: Exception with technical message for user display
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu of choices to the user
        ChangeLog: (Who, When, What)
        NWay,3.4.2025,Created function
        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        NWay,3.4.2025,Created function
        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        NWay, 3.5.2025,Created function
        :param student_data: list of dictionary rows that the input data will be added to
        :return: list of dictionary rows
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("Mismatch Values",e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.",e)

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the student and course names to the user
               ChangeLog: (Who, When, What)
               NWay,3.5.2025,Created function
               :param student_data: list of dictionary rows
               :return: None
               """
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(FILE_NAME, students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        IO.input_student_data(students)

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME,FILE_NAME_CSV,students)
        #Data was saved to a CSV file also as requested in bullet point 3 under Test on the assignment

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
