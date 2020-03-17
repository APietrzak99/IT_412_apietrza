from database_access import DB_Connect

my_db = DB_Connect('root','','python_projects')

def address_number(passed_address,address_bad_chars =  ["!",'"',"'","@","$","%","^","&","*","_","=","+","<",">","?",";","[","]","{","}"]):
    """passed address is validated to exist, then is tested for bad characters using the address_bad_chars list passed to it. if all characters within the address are good, then the return will be true
    arguments:
    passed_address
    returns
    True or False based on conditions met
    """
    if passed_address:
        address_has_bad_chars = False
        for char in passed_address:
            if char in address_bad_chars:
                address_has_bad_chars = True
        if not address_has_bad_chars:
            return True
        else:
            print("You did not enter a valid address. Please try again. ")
            return False
    else:
        print("You did not enter an address. Please try again. ")
        return False

def city_validate(passed_city):
    """ passed_city is validated to exist, then is tested for bad characters using the criteria established
    arguments:
    passed_city
    returns
    True or False based on conditions met"""
    if passed_city:
        city_has_bad_chars = False
        for char in passed_city:
            if not char.isalpha() and not char == "'":
                city_has_bad_chars = True
        if not city_has_bad_chars:
            return True
        else:
            print("You did not enter a valid city. Please try again. ")                
            return False           
    else:
        print("You did not enter a city. Please try again. ")
        return False

def company_title(passed_title):
    """passed title is validated to exist, then is returns true if it does
    arguments:
    passed_title
    returns
    True
    """
    if passed_title:
        return True
    else:
        pass
        return True

def data_add(f_name_prompt,l_name_prompt,title_prompt,address_prompt,city_prompt,state_prompt,zip_prompt,phone_prompt,second_phone_prompt,email_prompt):
    """passed values are added to both databases using sql insert statements.
    arguments:
    f_name_prompt,l_name_prompt,title_prompt,address_prompt,city_prompt,state_prompt,zip_prompt,phone_prompt,second_phone_prompt,email_prompt
    returns
    nothing
    """
    if title_prompt.strip() == "":
        title_prompt == "None"
    if second_phone_prompt.strip() == "":
        second_phone_prompt == "None"
    if email_prompt.strip() == "":
        email_prompt == "None"

    statement = ("INSERT INTO crm_data (f_name,l_name,address,city,state,zip,company,primary_phone,secondary_phone,email_address) VALUES (\""+ str(f_name_prompt) + "\",\""+ str(l_name_prompt) + "\",\""+ str(address_prompt) + "\",\""+ str(city_prompt) + "\",\"" + str(state_prompt) + "\",\"" + str(zip_prompt) + "\",\"" +  str(title_prompt) + "\",\""+ str(phone_prompt)+ "\",\"" + str(second_phone_prompt)+ "\",\""+ str(email_prompt)+"\")")
    my_db.executeQuery(statement)
    my_db.conn.commit()

    mailings_statement = ("INSERT INTO mailings (name,company,address) VALUES (\""+ str(f_name_prompt) + " "+  str(l_name_prompt) + "\",\""+ str(title_prompt)+ "\",\"" +  str(address_prompt)+"\")")
    my_db.executeQuery(mailings_statement)
    my_db.conn.commit()

    print("\nDATA ADDED\n")

def data_delete():
    """asks the user for the ID of a record to delete from the database they specify, 
    and will delete said record if they pick yes on the confirm_input prompt, will ignore change if they pick no
    arguments:
    none
    returns:
    none
    """
    database_prompt = input("Which database would you like to remove a record from? (CRM/Mailings) ")
    if database_prompt.title() == "Mailings":
        delete_prompt = input("Type the ID of the record you'd like to remove. ")
        if delete_prompt:
            confirm_input = input("Are you sure you'd like to delete this record? Y/N ")
            if confirm_input == "Y":
                try:
                    int(delete_prompt)
                    statement = ("DELETE FROM mailings WHERE mail_ID = " + str(delete_prompt))
                    my_db.executeQuery(statement)
                    my_db.conn.commit()
                    print("\nDATA DELETED\n")
                except:
                    print("You did not enter a valid ID. Please try again. ")
            else:
                pass
    elif database_prompt.upper() == "CRM":
        delete_prompt = input("Type the ID of the record you'd like to remove. ")
        if delete_prompt:
            confirm_input = input("Are you sure you'd like to delete this record? Y/N ")
            if confirm_input == "Y":
                try:
                    int(delete_prompt)
                    statement = ("DELETE FROM crm_data WHERE crm_ID = " + str(delete_prompt))
                    my_db.executeQuery(statement)
                    my_db.conn.commit()
                    print("\nDATA DELETED\n")
                except:
                    print("You did not enter a valid ID. Please try again. ")
            else:
                pass
    else:
        print("You did not enter a valid table to remove data from. ")

def data_edit(passed_column,passed_input,passed_id, passed_table):
    """is passed four pieces of data, that are then added to the sql statement below, which will update the record the user specified
    and add the new data that they have specified
    arguments:
    passed_column,passed_input,passed_id, passed_table
    returns:
    none"""
    if passed_table == "crm_data":
        statement = ("UPDATE " + passed_table + " SET "+ passed_column + " = \" " + passed_input + "\"WHERE crm_ID =\" " + passed_id + "\"")
        my_db.executeQuery(statement)
        my_db.conn.commit()
    elif passed_table.title() == "Mailings":
        statement = ("UPDATE " + passed_table + " SET "+ passed_column + " = \" " + passed_input + "\"WHERE mail_ID =\" " + passed_id + "\"")
        my_db.executeQuery(statement)
        my_db.conn.commit()
    print("\nDATA EDITED\n")

def data_print(): 
    """prints all data within the database the user picks line by line through the for loop established
    arguments:
    none
    returns
    none
    """
    database_prompt = input("Which database would you like to see all information from? (CRM/Mailings) ")
    if database_prompt.upper() == "CRM":
        my_result = my_db.executeSelectQuery("SELECT * FROM crm_data")
        for record in my_result:
            print("CRM ID: "+ str(record["crm_ID"]))
            print("Name: " + str(record["f_name"]) + " "+ str(record["l_name"]))
            print("Address: " + str(record["address"]))
            print("City: " + str(record["city"]))
            print("State: " + str(record["state"]))
            print("ZIP: " + str(record["zip"]))
            print("Company: " + str(record["company"]))
            print("Primary Phone: " + str(record["primary_phone"]))
            print("Second Phone: " + str(record["secondary_phone"]))
            print("Email: " + str(record["email_address"])+ "\n")
    elif database_prompt.title() == "Mailings":
        my_result = my_db.executeSelectQuery("SELECT * FROM mailings")
        for record in my_result:
            print("Mail ID: "+ str(record["mail_ID"]))
            print("Customer Name: " + record["name"])
            print("Company: " + record["company"])
            print("Address: " + str(record["address"])+ "\n")
    else:
        print("You did not enter a valid table. ")

def email_validate(passed_email,email_bad_chars =  ["!",'"',"'","#","$","%","^","&","*","(",")","=","+",",","<",">","/","?",";",":","[","]","{","}","\\"]):
    """passed email is validated to exist, then is tested for bad characters using the email_bad_chars list passed to it. if all characters within the address are good, then the return will be true
    arguments:
    passed_email
    returns
    True or False based on conditions met
    """
    if passed_email:
        email_has_bad_chars = False
        for char in passed_email:
            if char in email_bad_chars:
                email_has_bad_chars = True
        if not email_has_bad_chars:
            return True
        else:
            print("You did not enter a valid email. Please try again. ")
            return False
    else:
        pass
        return True

def name_edit_validate(passed_name):
    """ passed_name is validated to exist, then is tested for bad characters using the criteria established
    arguments:
    passed_name
    returns
    True or False based on conditions met"""
    if passed_name:
        name_has_bad_chars = False
        for char in passed_name:
            if not char.isalpha() and not char == "'" and not char == " ":
                name_has_bad_chars = True
        if not name_has_bad_chars:
            return True
        else:
            print("You did not enter a valid name. Please try again. ")                
            return False
    else:
        print("You did not enter a name. Please try again. ")
        return False

def name_validate(passed_name):
    """ passed_name is validated to exist, then is tested for bad characters using the criteria established
    arguments:
    passed_name
    returns
    True or False based on conditions met"""
    if passed_name:
        name_has_bad_chars = False
        for char in passed_name:
            if not char.isalpha() and not char == "'":
                name_has_bad_chars = True
        if not name_has_bad_chars:
            return True
        else:
            print("You did not enter a valid name. Please try again. ")                
            return False
    else:
        print("You did not enter a name. Please try again. ")
        return False

def phone_number(passed_phone,phone_good_chars =  ["1","2","3","4","5","6","7","8","9","0","-"]):
    """passed phone is validated to exist, then is tested for characters using the phone_good_chars list passed to it. if all characters within the phone number are good, then the return will be true
    arguments:
    passed_phone
    returns
    True or False based on conditions met
    """
    if passed_phone:
        phone_has_bad_chars = False
        for char in passed_phone:
            if char not in phone_good_chars:
                phone_has_bad_chars = True
        if not phone_has_bad_chars:
            return True
        else:
            print("You did not enter a valid phone number. Please try again. ")
            return False
    else:
        print("You did not enter a phone number. Please try again. ")
        return False

def second_phone_number(passed_phone,phone_good_chars =  ["1","2","3","4","5","6","7","8","9","0","-"]):
    """passed phone is validated to exist, then is tested for characters using the phone_good_chars list passed to it. if all characters within the phone number are good, then the return will be true
    arguments:
    passed_phone
    returns
    True or False based on conditions met
    """
    if passed_phone:
        phone_has_bad_chars = False
        for char in passed_phone:
            if char not in phone_good_chars:
                phone_has_bad_chars = True
        if not phone_has_bad_chars:
            return True
        else:
            print("You did not enter a valid phone number. Please try again. ")
            return False
    else:
        pass
        return True

def state_validate(passed_state):
    """ passed_state is validated to exist, then is tested for bad characters using the criteria established
    arguments:
    passed_state
    returns
    True or False based on conditions met"""
    if passed_state:
        if len(passed_state) == 2:
            state_has_bad_chars = False
            for char in passed_state:
                if not char.isalpha() or not char.isupper():
                    state_has_bad_chars = True
            if not state_has_bad_chars:
                return True
            else:
                print("You did not enter a valid state. Please ensure the state has two capital letters only and try again. ")                
                return False
        else:
            print("You entered the state incorrectly. Please enter the state as the two letter abbreviations only. ")
            return False
    else:
        print("You did not enter a state. Please try again. ")
        return False

def zip_validate(passed_zip):
    """ passed_zip is validated to exist, then is tested for bad characters using the criteria established
    arguments:
    passed_zip
    returns
    True or False based on conditions met"""
    if passed_zip:
        if len(passed_zip) == 4 or len(passed_zip) == 5:
            zip_has_bad_chars = False
            for char in passed_zip:
                if not char.isdigit():
                    zip_has_bad_chars = True
            if not zip_has_bad_chars:
                return True
            else:
                print("You did not enter a valid zip code. Please try again. ")                
                return False
        else:
            print("You entered the zip code incorrectly. Please try again. ")
            return False
    else:
        print("You did not enter a zip code. Please try again. ")
        return False

