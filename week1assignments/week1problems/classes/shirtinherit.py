from classes.clothing import Clothing

class ShirtInherit(Clothing):
    def __init__(self,size,color,quantity, type_info, message):
        super().__init__(size,color,quantity)
        self.type_info = type_info
        self.message = message

    def printMessage(self):
        print(self.message)