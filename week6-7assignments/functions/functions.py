from classes.database_access import DB_Connect

my_db = DB_Connect('root','','python_projects')

author_bad_chars = ["!",'"', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]

isbn_good_chars = ["1","2","3","4","5","6","7","8","9","0","-"]

def book_add(passed_title, passed_author, passed_isbn, passed_copies_purchased,passed_copies_checked_out,passed_retail):
    """passed values are added to book database using a sql insert statement. if passed_retail is empty, then the default value assigned will be 0
    arguments:
    passed_title, passed_author, passed_isbn, passed_copies_purchased,passed_copies_checked_out,passed_retail
    returns
    nothing
    """
    if passed_retail == "":
        passed_retail = "0"
    statement = ("INSERT INTO book_info (book_title,book_author,book_isbn,book_copies_purchased,book_copies_not_checked_out,book_retail) VALUES (\""+ str(passed_title) + "\",\""+ str(passed_author) + "\",\""+ str(passed_isbn) + "\",\""+ str(passed_copies_purchased) + "\",\"" + str(passed_copies_checked_out) + "\",\"" + str(passed_retail) + "\")")
    my_db.executeQuery(statement)
    my_db.conn.commit()

def book_author(passed_author):
    """passed author is validated to exist, then is tested for bad characters using the author_bad_chars list specified above
    arguments:
    passed_author
    returns
    True or False based on conditions met
    """
    if passed_author:
        author_has_bad_chars = False
        for char in passed_author:
            if char in author_bad_chars or char.isdigit():
                author_has_bad_chars = True
        if not author_has_bad_chars:
            return True
        else:
            print("You did not enter a valid author. Please try again. ")                
            return False
    else:
        print("You did not enter an author. Please try again. ")
        return False

def book_copies(passed_copies):
    """passed copies is validated to exist, then is converted to an int to test that it is a valid number
    arguments:
    passed_copies
    returns
    True or False based on conditions met
    """
    if passed_copies:
        try:
            int(passed_copies)
            return True
        except:
            print("You did not enter a valid number. Please try again. ")
            return False
    else:
        print("You did not enter a number. Please try again. ")
        return False

def book_delete():
    """asks the user for the ID of a book to delete from the database, and will delete said book
    arguments:
    none
    returns:
    none
    """
    delete_prompt = input("Type the ID of the book you'd like to remove. ")
    if delete_prompt:
        confirm_input = input("Are you sure you'd like to delete this book? Y/N ")
        if confirm_input == "Y":
            try:
                int(delete_prompt)
                statement = ("DELETE FROM book_info WHERE book_id = " + str(delete_prompt))
                my_db.executeQuery(statement)
                my_db.conn.commit()
            except:
                print("You did not enter a valid ID. Please try again. ")
        else:
            pass

def book_edit(passed_column,passed_input,passed_id):
    """is passed three pieces of data, that are then added to the sql statement below, which will update the record the user specified
    and add the new data that they have specified
    arguments:
    passed_column,passed_input,passed_id
    returns:
    none"""
    statement = ("UPDATE book_info SET "+ passed_column + " = \" " + passed_input + "\"WHERE book_id =\" " + passed_id + "\"")
    my_db.executeQuery(statement)
    my_db.conn.commit()

def book_isbn(passed_isbn):
    """passed isbn is validated to exist, then is tested for characters using the isbn_good_chars list specified above. if all characters within the isbn are good, then the return will be true
    arguments:
    passed_isbn
    returns
    True or False based on conditions met
    """
    if passed_isbn:
        isbn_has_bad_chars = False
        for char in passed_isbn:
            if char not in isbn_good_chars:
                isbn_has_bad_chars = True
        if not isbn_has_bad_chars:
            return True
        else:
            print("You did not enter a valid ISBN. Please try again. ")
            return False
    else:
        print("You did not enter an ISBN. Please try again. ")
        return False

def book_retail(passed_retail):
    """passed retail is validated to exist, then the datatype is converted to a float to test that it is a valid price
    arguments:
    passed_retail
    returns
    True or False based on conditions met
    """
    if passed_retail:
        try:
            float(passed_retail)
            return True
        except:
            print("You did not enter a valid number. Please try again. ")
            return False
    else:
        return True

def book_print(): 
    """prints all books within the database line by line through the for loop established
    arguments:
    none
    returns
    none
    """
    my_result = my_db.executeSelectQuery("SELECT * FROM book_info")
    for record in my_result:
        print("Book ID: "+ str(record["book_id"]))
        print("Book Title: " + record["book_title"])
        print("Book Author: " + record["book_author"])
        print("Book ISBN: " + str(record["book_isbn"]))
        print("Book Copies Purchased: " + str(record["book_copies_purchased"]))
        print("Book Copies Not Checked Out: " + str(record["book_copies_not_checked_out"]))
        print("Book Retail: $" + str(record["book_retail"])+ "\n")

def book_title(passed_title):
    """passed title is validated to exist, then is returns true if it does
    arguments:
    passed_title
    returns
    True or False based on conditions met
    """
    if passed_title:
        return True
    else:
        print("You did not enter a title. Please try again. ")
        return False
