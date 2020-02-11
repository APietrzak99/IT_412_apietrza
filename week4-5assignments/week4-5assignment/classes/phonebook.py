class PhoneBook():
    """Represents a phone book"""
    def __init__(self):
        self.PhoneBookList = []

    def name_validator(self,name_input):
        """Verifies name_input, which is used for both the first and last name, and verifies that it exists, and that it is all letters
        Arguments:
        name_input
        Returns
        True or false"""
        name_input = name_input.strip()

        if name_input:
            if name_input.isalpha():
                self.PhoneBookList.append({"Name": name_input})
                return True
            else:
                print("you did not enter a valid name. Please try again. ")
                return False
    
    def phone_validator(self,phone_input):
        """Verifies phone_input, verifies that it exists, that it is all digits, and that it is 10 digits long
        Arguments:
        phone_input
        Returns
        True or false"""
        phone_input = phone_input.strip()

        if phone_input:
            if phone_input.isdigit():
                if len(phone_input)== 10:
                    self.PhoneBookList.append({"Phone": phone_input})
                    return True
                else:
                    print("The phone number is not 10 digits long, please try again.")
                    return False
            else:
                print("You did not enter a valid phone number. ")
                return False
        else:
            print("You did not enter anything. ")
            return False

    def type_validator(self,type_input):
        """Verifies type_input, verifies that it exists, and then verifies that the user entered cell, office, or home for the phone type input
        Arguments:
        type_input
        Returns
        True or false"""
        type_input = type_input.strip()

        if type_input:
            if type_input == "home" or type_input == "cell" or type_input == "office":
                self.PhoneBookList.append({"Phone Type": type_input})
                return True
            else:
                print("you did not enter a valid type of phone number. ")
                return False