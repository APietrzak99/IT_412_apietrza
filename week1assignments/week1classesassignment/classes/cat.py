from classes.pet import Pet

class Cat(Pet):
    """A simple class for representing a cat"""

    def __init__(self,name,age):
        """initialize name and age variable/attributes for the cat"""
        super().__init__(name,age)