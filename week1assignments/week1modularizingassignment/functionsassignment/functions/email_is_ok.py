email_bad_chars=["!",'"',"'","#","$","%","^","&","*","(",")","=","+",",","<",">","/","?",";",":","[","]","{","}",")",'\\']

def email_is_ok(passed_email):
    """processes an input string, checks that the input is not null, then checks that the input does not have bad chars from the list, email_bad_chars
    Arguments:
        passed_email (input)
    returns:
        True or False for the value specified based on the input the user enters
    """

    if passed_email:
        has_bad_chars = False
        for character in passed_email:
            if character in email_bad_chars:
                has_bad_chars = True
        if not has_bad_chars:
            return True
        else:
            print("Your email has bad characters in it")
            return False
                
    else:
        print("You did not provide a name")
        return False
