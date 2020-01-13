name_bad_chars=["!",'"',"@","#","$","%","^","&","*","(",")","_","=","+",",","<",">","/","?",";",":","[","]","{","}",")",'\\']
def name_is_ok(passed_name):
    """processes an input string, checks that the input is not null, then checks that the input does not have bad chars from the list, name_bad_chars, 
    and also checks that the input has no characters that are digits
    Arguments:
        passed_name (input)
    returns:
        True or False based on the input the user enters
    """
    if passed_name:
        has_bad_chars = False
        for character in passed_name:
            if character in name_bad_chars or character.isdigit():
                has_bad_chars = True
        if not has_bad_chars:
            return True
        else:
            print("Your name has bad characters in it")
            return False
                
    else:
        print("You did not provide a name")
        return False