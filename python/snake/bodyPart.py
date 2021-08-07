class BodyPart:
	def __init__(self, head):
		self.dimensions = 5;
		self.head = head;

	def getDimensions(self):
		return self.dimensions;

	def isHead(self):
		return self.head
