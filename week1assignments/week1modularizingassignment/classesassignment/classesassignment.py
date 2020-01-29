from classes.person import Person
from classes.instructor import Instructor
from classes.student import student
from classes.validator import Validator, college_records

#set up an instance of validator class
validate_value = Validator()

#program will run until this is set to false
program_running = True
while program_running == True:
    initial_input_correct = False
    while not initial_input_correct:
#set up initial input tag that asks for student, instructor, or the end of the program
        initial_input = input("Enter S if you're a student or I if you're an instructor. Enter end if you would like the program to stop.")
        if initial_input == 'S':
            initial_input_entered = validate_value.info_is_ok("Student")
            student_id_correct = False
            while not student_id_correct:
                student_id = input("Please enter your student ID: ")
                student_id_correct = validate_value.id_is_ok(student_id, 7)
                if student_id_correct == True:
                    program_studying = input("Please enter the program of study you are in: ")
                    if program_studying:
                        program_studying_entered = validate_value.info_is_ok(program_studying)
                        initial_input_correct = True
                    else:
                        program_studying = input("You did not enter a program of study: ")
#instructor while loop
        if initial_input == 'I':
            initial_input_entered = validate_value.info_is_ok("Instructor")
            instructor_id_correct = False
            while not instructor_id_correct:
                instructor_id = input("Please enter your instructor ID: ")
                instructor_id_correct = validate_value.id_is_ok(instructor_id, 5)
                if instructor_id_correct == True:
                    university_graduated = input('Please enter the last institution you graduated from: ')
                    if university_graduated:
                        university_graduated_entered = validate_value.info_is_ok(university_graduated)
                        highest_degree = input("Please enter the highest degree you earned: ")
                        if highest_degree:
                            highest_degree_entered = validate_value.info_is_ok(highest_degree)
                            initial_input_correct = True
                        else:
                            highest_degree = input("You did not enter your degree: ")
                    else:
                        university_graduated = input("You did not enter an institution: ")

        if initial_input == 'end':
            Validator.displayInformation(college_records)
            program_running == False
    
#name while loop
    person_name_correct = False
    while not person_name_correct:
        person_name = input("Please enter your name: ")
        person_name_correct = validate_value.name_is_ok(person_name)
        
    
#email while loop
    person_email_correct = False
    while not person_email_correct:
        person_email = input("Please enter your email: ")
        person_email_correct = validate_value.email_is_ok(person_email)