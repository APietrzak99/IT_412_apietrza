from classes.person import Person

class student(Person):
    """a simple class meant to represent a student"""
    def __init__(self,passed_id,passed_name,passed_email):
        """call name, email, id variables and attributes from person class """
        super().__init__(passed_id, passed_email,passed_name)