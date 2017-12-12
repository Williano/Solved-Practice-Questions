# Script: CourseInformation.py
# Description: This program creates a dictionary containing course numbers,
#              the meeting times of each course, the names of the instructors
#              that teach each course and the room numbers of the rooms       
#              where the courses meet.Enter any of these course numbers to
#              get it's room number, it's instructor and meeting time.
#              These are the course numbers: CS101, CS102, CS103, NT110 and CM241. 
# Programmer: William Kpabitey Kwabla.
# Date: 15.02.17


# Defining the main function.
def main():

    # Calling the intro function to display what the program does.
    intro()

    # Creating a dictionary to store room numbers.
    room_numbers = {"CS101":"3004", "CS102":"4501", "CS103":"6755", "NT110":"1244", "CM241":"1411" }

    # Creating a dictionary to store instructors.
    instructors = {"CS101":"Haynes", "CS102":"Alvarado", "CS103":"Rich", "NT110":"Burke", "CM241":"Lee"}

    # Creating a dictionary to store meeting times.
    meeting_times = {"CS101":"8:00 a.m", "CS102":"9:00 a.m", "CS103":"10:00 a.m", "NT110":"11:00 a.m", "CM241":"1.00 p.m"}

    # Asking user for course number.
    print()
    course_number = input("\t\t\t\tPlease Enter the course number: ")
    print()

    # Displaying course information for user by calling the room number,instructor,meeting time functions
    # and passing the course number from the user and their respective dictionaries for each of the function
    # which display the room number,instructor and meeting time to the user.
    room_number(room_numbers,course_number)
    instructor(instructors,course_number)
    meeting_time(meeting_times,course_number)
    

    
# Defining the intro function to display what the program does.
def intro():
    print("\t\t\t\t**********************************************************************")
    print("\t\t\t\t* This program creates a dictionary containing course numbers,       *")
    print("\t\t\t\t* the meeting times of each course, the names of the instructors     *")
    print("\t\t\t\t* that teach each course and the room numbers of the rooms           *")
    print("\t\t\t\t* where the courses meet. Enter any of these course numbers to       *") 
    print("\t\t\t\t* get it's room number, it's instructor and meeting time.            *") 
    print("\t\t\t\t* These are the course numbers: CS101, CS102, CS103, NT110 and CM241 *")
    print("\t\t\t\t**********************************************************************")


# Defining the room number function and passing the room numbers dictionary and course number
# from user as parameter variables which then return the room number for the course to the fucntion.
def room_number(room_numbers,course):
    for key in room_numbers:
        if key == course:
            print("\t\t\t\tThe room number for", course, "is",room_numbers[key])


# Defining the instructor function and passing the instructors dictionary and course number
# from user as parameter variables which then return the instructor for the course to the fucntion.
def instructor(instructors,course):
    for key in instructors:
        if key == course:
            print("\t\t\t\tThe instructor for", course, "is",instructors[key])


# Defining the meeting time function and passing the meeting times dictionary and course number
# from user as parameter variables which then return the meeting time for the course to the fucntion.
def meeting_time(meeting_times,course):
    for key in meeting_times:
        if key == course:
            print("\t\t\t\tThe meeting time for", course, "is",meeting_times[key])

    

# Calling the main function to execute the program.
main()
