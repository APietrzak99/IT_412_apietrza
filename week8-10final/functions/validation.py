from classes.database_access import DB_Connect

my_db = DB_Connect('root','','python_projects')

# def book_add():
#     """passed values are added to book database using a sql insert statement. if passed_retail is empty, then the default value assigned will be 0
#     arguments:
#     passed_title, passed_author, passed_isbn, passed_copies_purchased,passed_copies_checked_out,passed_retail
#     returns
#     nothing
#     """
#     statement = ("INSERT INTO book_info (book_title,book_author,book_isbn,book_copies_purchased,book_copies_not_checked_out,book_retail) VALUES (\""+ str(passed_title) + "\",\""+ str(passed_author) + "\",\""+ str(passed_isbn) + "\",\""+ str(passed_copies_purchased) + "\",\"" + str(passed_copies_checked_out) + "\",\"" + str(passed_retail) + "\")")
#     my_db.executeQuery(statement)
#     my_db.conn.commit()

# def book_delete():
#     """asks the user for the ID of a book to delete from the database, and will delete said book
#     arguments:
#     none
#     returns:
#     none
#     """
#     delete_prompt = input("Type the ID of the book you'd like to remove. ")
#     if delete_prompt:
#         confirm_input = input("Are you sure you'd like to delete this book? Y/N ")
#         if confirm_input == "Y":
#             try:
#                 int(delete_prompt)
#                 statement = ("DELETE FROM book_info WHERE book_id = " + str(delete_prompt))
#                 my_db.executeQuery(statement)
#                 my_db.conn.commit()
#             except:
#                 print("You did not enter a valid ID. Please try again. ")
#         else:
#             pass

# def book_edit(passed_column,passed_input,passed_id):
#     """is passed three pieces of data, that are then added to the sql statement below, which will update the record the user specified
#     and add the new data that they have specified
#     arguments:
#     passed_column,passed_input,passed_id
#     returns:
#     none"""
#     statement = ("UPDATE book_info SET "+ passed_column + " = \" " + passed_input + "\"WHERE book_id =\" " + passed_id + "\"")
#     my_db.executeQuery(statement)
#     my_db.conn.commit()


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
    True or False based on conditions met
    """
    if passed_title:
        return True
    else:
        pass
        return True

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
            print("You entered the zip codee incorrectly. Please try again. ")
            return False
    else:
        print("You did not enter a zip code. Please try again. ")
        return False


# def book_print(): 
#     """prints all books within the database line by line through the for loop established
#     arguments:
#     none
#     returns
#     none
#     """
#     my_result = my_db.executeSelectQuery("SELECT * FROM book_info")
#     for record in my_result:
#         print("Book ID: "+ str(record["book_id"]))
#         print("Book Title: " + record["book_title"])
#         print("Book Author: " + record["book_author"])
#         print("Book ISBN: " + str(record["book_isbn"]))
#         print("Book Copies Purchased: " + str(record["book_copies_purchased"]))
#         print("Book Copies Not Checked Out: " + str(record["book_copies_not_checked_out"]))
#         print("Book Retail: $" + str(record["book_retail"])+ "\n")
