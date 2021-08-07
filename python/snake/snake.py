# Class for snake object
from bodyPart import BodyPart
class Snake:
	#Constructor
	def __init__(self):
		self.size = 4;
		self.structure = [0]*self.size;
		self.createBody();
	#getter	
	def getSize(self):
		return self.size;
	#setter
	def setSize(self, additionValue):
		self.size += additionValue;

	def createBody(self):
		self.structure[0] = BodyPart(1)
		for i in range(1,self.getSize()):
			self.structure[i] = BodyPart(0);
	#dor debugging
	def check(self):
		for i in range(self.getSize()):
			print(self.structure[i].isHead())