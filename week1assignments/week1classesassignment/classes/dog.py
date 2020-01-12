from classes.pet import Pet

class Dog(Pet):
    """A simple class for representing a dog"""
    def __init__(self, name, age, breed):
        """initialize name and age attributes/variables for the dog"""
        super().__init__(name,age)
        self.breed = breed

    def placeDogInCarrier(self):
        """This represents placing the dog in the carrier"""
        print(self.name + " is in the car carrier!")

    def takeToVet(self):
        """contains all of the tasks needed to get the dog to the vet"""
        self.placeDogInCarrier()
        self.__visitVet()

    def __visitVet(self):
        """represents the act of taking the dog to the vet"""
        print(self.name + " is on the way to the vet!")