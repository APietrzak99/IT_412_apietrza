class Clothing():
	def __init__(self,size,color,quantity = 1):
		self.size = size
		self.color = color
		self.quantity = quantity

	def quantityDecrease(self,number):
		self.quantity = self.quantity - number
		return self.quantity

	def quantityIncrease(self,number):
		self.quantity = number + self.quantity
		return self.quantity

	def shirtInfo(self):
		print(self.color + " " + self.size)