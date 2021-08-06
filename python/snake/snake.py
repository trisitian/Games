# Class for snake object
class Snake:
	#Constructor
	def __init__(self):
		self.size = 4;
	#getter	
	def getSize(self):
		return self.size;
	#setter
	def setSize(self, additionValue):
		self.size += additionValue;