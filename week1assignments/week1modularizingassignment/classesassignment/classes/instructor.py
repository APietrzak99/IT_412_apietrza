from classes.person import Person

class Instructor:
    """a simple class meant to represent an instructor"""
    def __init__(self,passed_id,passed_name,passed_email):
        """call name, email, id variables and attributes from person class """
        super().__init__(passed_id, passed_email,passed_name)