from functions.id_is_ok import id_is_ok
from functions.name_is_ok import name_is_ok
from functions.email_is_ok import email_is_ok

#sets up the amount of times the program will run
program_counter = 0

#empty list set up to append to
complete_employee_info = []

address_bad_chars=["!",'"',"'","@","$","%","^","&","*","(",")","_","=","+","<",">","?",";",":","[","]","{","}",")"]


while program_counter < 5:

    employee_id_correct = False
    while not employee_id_correct:
        employee_id = input("Please enter your employee ID: ")
        employee_id_correct = id_is_ok(employee_id)

    employee_name_correct = False
    while not employee_name_correct:
        employee_name = input("Please enter your name: ")
        employee_name_correct = name_is_ok(employee_name)

    employee_email_correct = False
    while not employee_email_correct:
        employee_email = input("Please enter your email: ")
        employee_email_correct = email_is_ok(employee_email)

    employee_address_correct = False
    while not employee_address_correct:
        employee_address = input("Please enter your address (not required):  ")
        #for some reason, whenever I move everything past this line into a function on it's own, it errors out and says I am using the employee_address variable
# before initializing. also tells me the break is invalid.  
        if employee_address:
            if employee_address.isalnum():
                for character in employee_address:
                    if character not in address_bad_chars:
                        employee_address_correct = True
                    else:
                        employee_address = input("Your address was not entered properly. Please try again.")
                        employee_address_correct = False
        else:
            break

#append values taken from inputs to list. become a dictionary through pairs set up
    complete_employee_info.append({'Employee ID': employee_id, 'Employee Name': employee_name, 'Employee Email Address': employee_email, 'Employee Address': employee_address})
    program_counter +=1

if employee_address_correct == True & employee_email_correct == True & employee_id_correct == True & employee_name_correct == True:
    print("Hello, " + employee_name + ". Your Employee ID is " + employee_id + ", and your email address is " + employee_email + ". Your Address is " + employee_address)
elif employee_address_correct == False & employee_email_correct == True & employee_id_correct == True & employee_name_correct == True:
    print("Hello, " + employee_name + ". Your Employee ID is " + employee_id + ", and your email address is " + employee_email + ". You did not provide an address." )

print(complete_employee_info)