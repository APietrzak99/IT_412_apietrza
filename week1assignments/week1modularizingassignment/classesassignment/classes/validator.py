
name_bad_chars=["!",'"',"@","#","$","%","^","&","*","(",")","_","=","+",",","<",">","/","?",";",":","[","]","{","}",")",'\\']
email_bad_chars=["!",'"',"'","#","$","%","^","&","*","(",")","=","+",",","<",">","/","?",";",":","[","]","{","}",")",'\\']
college_records = []
class Validator: 
    """a class meant to act as validation for the inputs in the main program"""
    def id_is_ok(self,passed_id,passed_length):
        """define id_is_ok input check using passed_id and passed_length arguments """
        if passed_id:
            try:
                int(passed_id)
                if len(passed_id) <= passed_length:
                    correct_id = passed_id
                    college_records.append(correct_id)
                    return True
                else:
                    print('Your ID was entered incorrectly. Please try again.')
                    return False
            except:
                print("You did not enter your ID correctly. Please try again.")
                False
        else:
            print('Your ID was not entered. Please try again.')
            False

    def name_is_ok(self,passed_name):
        """define name_is_ok input check using passed_name argument """
        if passed_name:
            has_bad_chars = False
            for character in passed_name:
                if character in name_bad_chars or character.isdigit():
                    has_bad_chars = True
            if not has_bad_chars:
                college_records.append(passed_name)
                return True
            else:
                print("Your name has bad characters in it")
                return False          
        else:
            print("You did not provide a name")
            return False
        
    def email_is_ok(self,passed_email):
        """define email_is_ok input check using passed_email argument """
        if passed_email:
            has_bad_chars = False
            for character in passed_email:
                if character in email_bad_chars:
                    has_bad_chars = True
            if not has_bad_chars:
                college_records.append(passed_email)
                return True
            else:
                print("Your email has bad characters in it")
                return False          
        else:
            print("You did not provide a email")
            return False

    def info_is_ok(self,passed_info):
        """define info_is_ok input check using passed_info argument """
        if passed_info:
            college_records.append(passed_info)
            return True
        else:
            return False

    def displayInformation(self):
        print(college_records)