#function imports
from functions.validation import *

#initial input to start the program
initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Import a new data file\n 2. Show data currently in a database. \n 3. Add a record to the databases. \n 4. Edit a record.\n 5. Remove a record. \n 6. Exit Program.\n ")

#program will keep running until the user types 5 into the initial input 
while initial_prompt != str(6):
    if initial_prompt == str(1):
        #build import structure here
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Import a new data file\n 2. Show data currently in a database. \n 3. Add a record to the databases. \n 4. Edit a record. \n 5. Remove a record. \n 6. Exit Program.\n   ")
    if initial_prompt == str(2):
        data_print()
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Import a new data file\n 2. Show data currently in a database. \n 3. Add a record to the databases. \n 4. Edit a record. \n 5. Remove a record. \n 6. Exit Program.\n   ")
    #typing 3 will start asking users each individual piece needed to populate the database and will send them to functions that will verify that they are valid inputs
    if initial_prompt == str(3):
        f_name_correct = False
        while not f_name_correct:
            f_name_prompt = input("Please enter your first name. ")
            f_name_correct = name_validate(f_name_prompt)
        l_name_correct = False
        while not l_name_correct:
            l_name_prompt = input("Please enter your last name. ")
            l_name_correct = name_validate(l_name_prompt)
        title_correct = False
        while not title_correct:
            title_prompt = input("Please enter the title of your company. This may be left blank if you like. ")
            title_correct = company_title(title_prompt)
        address_correct = False
        while not address_correct:
            address_prompt = input("Please enter your address. ")
            address_correct = address_number(address_prompt)
        city_correct = False
        while not city_correct:
            city_prompt = input("Please enter your city. ")
            city_correct = city_validate(city_prompt)
        state_correct = False
        while not state_correct:
            state_prompt = input("Please enter your state as a two letter abbreviation. (MI, AZ, etc.) ")
            state_correct = state_validate(state_prompt)
        zip_correct = False
        while not zip_correct:
            zip_prompt = input("Please enter your ZIP code. ")
            zip_correct = zip_validate(zip_prompt)
        phone_correct = False
        while not phone_correct:
            phone_prompt = input("Please enter your phone number. ")
            phone_correct = phone_number(phone_prompt)
        second_phone_correct = False
        while not second_phone_correct:
            second_phone_prompt = input("Please enter a second phone number. You may leave this blank if you would like. ")
            second_phone_correct = second_phone_number(second_phone_prompt)
        email_correct = False
        while not email_correct:
            email_prompt = input("Please enter an email address. You may leave this blank if you would like. ")
            email_correct = email_validate(email_prompt)
        data_add(f_name_prompt,l_name_prompt,title_prompt,address_prompt,city_prompt,state_prompt,zip_prompt,phone_prompt,second_phone_prompt,email_prompt)
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Import a new data file\n 2. Show data currently in a database. \n 3. Add a record to the databases. \n 4. Edit a record.\n 5. Remove a record. \n 6. Exit Program.\n  ")
    if initial_prompt == str(4):
        table_prompt = input("Which table would you like to edit? (Mailings or CRM) ")
        edit_column_prompt = input("Please type which column you'd like to edit. ")
        edit_id_prompt = input("Please type the ID of the field you'd like to edit. ")
        if table_prompt.upper() == "CRM":
            if edit_column_prompt.title() == "First Name":
                f_name_correct = False
                while not f_name_correct:
                    f_name_prompt = input("Please enter the new first name. ")
                    f_name_correct = name_validate(f_name_prompt)
                data_edit("f_name", f_name_prompt, edit_id_prompt, "crm_data")
            elif edit_column_prompt.title() == "Last Name":
                l_name_correct = False
                while not l_name_correct:
                    l_name_prompt = input("Please enter the new last name. ")
                    l_name_correct = name_validate(l_name_prompt)
                data_edit("l_name", l_name_prompt, edit_id_prompt, "crm_data")
            elif edit_column_prompt.title() == "Company Title":
                title_correct = False
                while not title_correct:
                    title_prompt = input("Please enter the new title of the company. ")
                    title_correct = company_title(title_prompt)
                data_edit("company", title_prompt, edit_id_prompt, "crm_data")
            elif edit_column_prompt.title() == "Address":    
                address_correct = False
                while not address_correct:
                    address_prompt = input("Please enter the new address. ")
                    address_correct = address_number(address_prompt)
                data_edit("address", address_prompt, edit_id_prompt, "crm_data")
            elif edit_column_prompt.title() == "City":    
                city_correct = False
                while not city_correct:
                    city_prompt = input("Please enter the new city. ")
                    city_correct = city_validate(city_prompt)
                data_edit("city", city_prompt, edit_id_prompt,"crm_data")
            elif edit_column_prompt.title() == "State":    
                state_correct = False
                while not state_correct:
                    state_prompt = input("Please enter the new state as a two letter abbreviation. ")
                    state_correct = state_validate(state_prompt)
                data_edit("state", state_prompt, edit_id_prompt, "crm_data")
            elif edit_column_prompt.title() == "Zip Code":    
                zip_correct = False
                while not zip_correct:
                    zip_prompt = input("Please enter the new ZIP code. ")
                    zip_correct = zip_validate(zip_prompt)
                data_edit("zip", zip_prompt, edit_id_prompt, "crm_data")
            elif edit_column_prompt.title() == "Phone Number":
                phone_correct = False
                while not phone_correct:
                    phone_prompt = input("Please enter the new phone number. ")
                    phone_correct = phone_number(phone_prompt)
                data_edit("primary_phone", phone_prompt, edit_id_prompt,"crm_data")
            elif edit_column_prompt.title() == "Secondary Phone":    
                phone_correct = False
                while not phone_correct:
                    phone_prompt = input("Please enter the new phone number. ")
                    phone_correct = phone_number(phone_prompt)
                data_edit("secondary_phone", phone_prompt, edit_id_prompt, "crm_data")
            elif edit_column_prompt.title() == "Email Address" or edit_column_prompt.title() == "Email":    
                email_correct = False
                while not email_correct:
                    email_prompt = input("Please enter the new email address. ")
                    email_correct = email_validate(email_prompt)
                data_edit("email_address", email_prompt, edit_id_prompt, "crm_data")
            else:
                print("You did not enter a valid record to edit. ")  
        elif table_prompt.title() == "Mailings":
            if edit_column_prompt.title() == "Name":
                name_correct = False
                while not name_correct:
                    name_prompt = input("Please enter the new name. ")
                    name_correct = name_edit_validate(name_prompt)
                data_edit("name", name_prompt, edit_id_prompt, table_prompt)
            elif edit_column_prompt.title() == "Company":
                title_correct = False
                while not title_correct:
                    title_prompt = input("Please enter the new title of the company. ")
                    title_correct = company_title(title_prompt)
                data_edit("company", title_prompt, edit_id_prompt, table_prompt)
            elif edit_column_prompt.title() == "Address":    
                address_correct = False
                while not address_correct:
                    address_prompt = input("Please enter the new address. ")
                    address_correct = address_number(address_prompt)
                data_edit("address", address_prompt, edit_id_prompt, table_prompt)
            else:
                print("You did not enter a valid record to edit. ")
        else:
            print("You did not enter a valid table to edit. ")  
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Import a new data file\n 2. Show data currently in a database. \n 3. Add a record to the databases. \n 4. Edit a record. \n 5. Remove a record. \n 6. Exit Program.\n  ")
    if initial_prompt == str(5):
        data_delete()
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Import a new data file\n 2. Show data currently in a database. \n 3. Add a record to the databases. \n 4. Edit a record. \n 5. Remove a record. \n 6. Exit Program.\n  ")
    #typing 6 exits the program
    if initial_prompt == str(6):
        exit()