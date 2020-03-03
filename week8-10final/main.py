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
        #build print structure here
        #data_print()
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
        # data_add(title_prompt,author_prompt,isbn_prompt,copies_purchased_prompt,copies_not_checked_out_prompt,retail_prompt)
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Import a new data file\n 2. Show data currently in a database. \n 3. Add a record to the databases. \n 4. Edit a record.\n 5. Remove a record. \n 6. Exit Program.\n  ")
    if initial_prompt == str(4):
        table_prompt = input("Which table would you like to edit? (Mailings or CRM) ")
        edit_column_prompt = input("Please type which record you'd like to edit. ")
        if edit_column_prompt == "First Name":
            f_name_correct = False
            while not f_name_correct:
                f_name_prompt = input("Please enter the new first name. ")
                f_name_correct = name_validate(f_name_prompt)
        #    book_edit("book_author", author_prompt, edit_id_prompt)
        if edit_column_prompt == "Last Name":
            l_name_correct = False
            while not l_name_correct:
                l_name_prompt = input("Please enter the new last name. ")
                l_name_correct = name_validate(l_name_prompt)
        #    book_edit("book_author", author_prompt, edit_id_prompt)
        if edit_column_prompt == "Company Title":
            title_correct = False
            while not title_correct:
                title_prompt = input("Please enter the new title of the company. ")
                title_correct = company_title(title_prompt)
        #     book_edit("book_title", title_prompt, edit_id_prompt)
        if edit_column_prompt == "Address":    
            address_correct = False
            while not address_correct:
                address_prompt = input("Please enter the new address. ")
                address_correct = address_number(address_prompt)
        #     book_edit("book_copies_purchased", copies_purchased_prompt, edit_id_prompt)
        if edit_column_prompt == "City":    
            city_correct = False
            while not city_correct:
                city_prompt = input("Please enter the new city. ")
                city_correct = city_validate(city_prompt)
        #     book_edit("book_copies_purchased", copies_purchased_prompt, edit_id_prompt)
        if edit_column_prompt == "State":    
            state_correct = False
            while not state_correct:
                state_prompt = input("Please enter the new state as a two letter abbreviation. ")
                state_correct = state_validate(state_prompt)
        #     book_edit("book_copies_purchased", copies_purchased_prompt, edit_id_prompt)
        if edit_column_prompt == "Zip Code":    
            zip_correct = False
            while not zip_correct:
                zip_prompt = input("Please enter the new ZIP code. ")
                zip_correct = zip_validate(zip_prompt)
        #     book_edit("book_copies_purchased", copies_purchased_prompt, edit_id_prompt)
        if edit_column_prompt == "Phone Number":
            phone_correct = False
            while not phone_correct:
                phone_prompt = input("Please enter the new phone number. ")
                phone_correct = phone_number(phone_prompt)
        #    book_edit("book_isbn", isbn_prompt, edit_id_prompt)
        if edit_column_prompt == "Email Address" or edit_column_prompt == "Email":    
            email_correct = False
            while not email_correct:
                email_prompt = input("Please enter the new email address. ")
                email_correct = email_validate(email_prompt)
        #     book_edit("book_copies_purchased", copies_purchased_prompt, edit_id_prompt)
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Import a new data file\n 2. Show data currently in a database. \n 3. Add a record to the databases. \n 4. Edit a record. \n 5. Remove a record. \n 6. Exit Program.\n  ")
    if initial_prompt == str(5):
        database_prompt = input("Which database would you like to remove data from? ")
        record_prompt = input("Which record would you like to remove data from? ")
        field_prompt = input("Which field would you like to remove? ")
    #    remove_data(database_prompt,record_prompt,field_prompt)
    #typing 6 exits the program
    if initial_prompt == str(6):
        exit()