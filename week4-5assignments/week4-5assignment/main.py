from classes.phonebook import PhoneBook

my_phone = PhoneBook()

program_running = True

while program_running is True:
    initial_input = input("Are you done adding phone numbers? (Y/N) ")
    if initial_input == "N":
        name_input = input("Please type your name without any spaces: ")
        check_name_true = my_phone.name_validator(name_input)
        while check_name_true == True:
            phone_input = input("Please enter your phone number with no spaces: ")
            validate_phone = my_phone.phone_validator(phone_input)
            while validate_phone == True:
                type_input = input("Please enter your phone number type (home, office, or cell): ")
                validate_type = my_phone.type_validator(type_input)
                if validate_type is True:
                    validate_phone = False
                    check_name_true = False
    elif initial_input == "Y":
        print(my_phone.PhoneBookList)
        program_running = False
    else:
        print("You did not enter a valid input. ")
            