def id_is_ok(passed_id):
    """processes an input string, checks that the input is not null, then checks the input's length based on , email_bad_chars
    Arguments:
        passed_id (input)
    returns:
        True or False based on the input checks in place, if the value is null or is longer than 7 characters, than false will be returned
    """
    if passed_id:
        try:
            int(passed_id)
            if len(passed_id) <= 7:
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