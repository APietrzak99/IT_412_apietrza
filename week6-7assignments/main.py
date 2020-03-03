#function imports
from functions.functions import book_print
from functions.functions import book_delete
from functions.functions import book_author
from functions.functions import book_edit
from functions.functions import book_title
from functions.functions import book_isbn
from functions.functions import book_copies
from functions.functions import book_retail
from functions.functions import book_add

#initial input t ostart the program
initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Show All Books\n 2. Add a Book. \n 3. Edit A Book. \n 4. Remove A Book. \n 5. Exit Program.\n ")

#program will keep running until the user types 5 into the initial input 
while initial_prompt != str(5):
    #typing 1 will start the book_print function that prints all books in the database
    if initial_prompt == str(1):
        book_print()
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Show All Books\n 2. Add a Book. \n 3. Edit A Book. \n 4. Remove A Book. \n 5. Exit Program.\n  ")
    #typing 2 will start asking users each individual piece needed to populate the database and will send them to functions that will verify that they are valid inputs
    if initial_prompt == str(2):
        title_correct = False
        while not title_correct:
            title_prompt = input("Please enter the title of the book. ")
            title_correct = book_title(title_prompt)
        author_correct = False
        while not author_correct:
            author_prompt = input("Please enter the author of the book. ")
            author_correct = book_author(author_prompt)
        isbn_correct = False
        while not isbn_correct:
            isbn_prompt = input("Please enter the ISBN of the book. ")
            isbn_correct = book_isbn(isbn_prompt)
        copies_purchased_correct = False
        while not copies_purchased_correct:
            copies_purchased_prompt = input("Please enter the number of copies of the book that were purchased. ")
            copies_purchased_correct = book_copies(copies_purchased_prompt)
        copies_not_checked_out_correct = False
        while not copies_not_checked_out_correct:
            copies_not_checked_out_prompt = input("Please enter the number of copies of the book that are not checked out. ")
            copies_not_checked_out_correct = book_copies(copies_not_checked_out_prompt)
        retail_correct = False
        while not retail_correct:
            retail_prompt = input("Please enter the retail price of the book as a decimal. You do not have to enter this if you don't want to. ")
            retail_correct = book_retail(retail_prompt)
        book_add(title_prompt,author_prompt,isbn_prompt,copies_purchased_prompt,copies_not_checked_out_prompt,retail_prompt)
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Show All Books\n 2. Add a Book. \n 3. Edit A Book. \n 4. Remove A Book. \n 5. Exit Program.\n  ")
    #typing 3 will ask the user the ID of the book they'd like to edit and what they'd like to change it to
    #the input will then be verified as valid through each respective piece of data's verifying function 
    # this will then be passed to the book_edit function which will commit the data to the database
    if initial_prompt == str(3):
        edit_id_prompt = input("Please enter the ID of the book you'd like to edit. ")
        edit_column_prompt = input("Please type which part you'd like to edit. (Book Title, Book Author, Book ISBN, Copies Purchased, Copies Not Checked Out, Retail) ")
        if edit_column_prompt == "Book Title":
            title_correct = False
            while not title_correct:
                title_prompt = input("Please enter the new title of the book. ")
                title_correct = book_title(title_prompt)
            book_edit("book_title", title_prompt, edit_id_prompt)
        if edit_column_prompt == "Book Author":
            author_correct = False
            while not author_correct:
                author_prompt = input("Please enter the new author of the book. ")
                author_correct = book_author(author_prompt)
            book_edit("book_author", author_prompt, edit_id_prompt)
        if edit_column_prompt == "Book ISBN":
            isbn_correct = False
            while not isbn_correct:
                isbn_prompt = input("Please enter the new ISBN of the book. ")
                isbn_correct = book_isbn(isbn_prompt)
            book_edit("book_isbn", isbn_prompt, edit_id_prompt)
        if edit_column_prompt == "Copies Purchased":    
            copies_purchased_correct = False
            while not copies_purchased_correct:
                copies_purchased_prompt = input("Please enter the new number of copies of the book that were purchased. ")
                copies_purchased_correct = book_copies(copies_purchased_prompt)
            book_edit("book_copies_purchased", copies_purchased_prompt, edit_id_prompt)
        if edit_column_prompt == "Copies Not Checked Out":
            copies_not_checked_out_correct = False
            while not copies_not_checked_out_correct:
                copies_not_checked_out_prompt = input("Please enter the new number of copies of the book that are not checked out. ")
                copies_not_checked_out_correct = book_copies(copies_not_checked_out_prompt)
            book_edit("book_copies_not_checked_out", copies_not_checked_out_prompt, edit_id_prompt)
        if edit_column_prompt == "Retail":
            retail_correct = False
            while not retail_correct:
                retail_prompt = input("Please enter the new retail price of the book as a decimal. ")
                retail_correct = book_retail(retail_prompt)
            book_edit("book_retail", retail_prompt, edit_id_prompt)
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Show All Books\n 2. Add a Book. \n 3. Edit A Book. \n 4. Remove A Book. \n 5. Exit Program.\n  ")
    #typing 4 will call the book_delete function and will return the initial prompt when it is complete 
    if initial_prompt == str(4):
        book_delete()
        initial_prompt = input("Type the number of the option you'd like to pick. \n 1. Show All Books\n 2. Add a Book. \n 3. Edit A Book. \n 4. Remove A Book. \n 5. Exit Program.\n  ")
    #typing 5 exits the program
    if initial_prompt == str(5):
        exit()