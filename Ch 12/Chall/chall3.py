class Triangle:
	def __init__(self, h, b):
		self.height = h
		self.base = b

	def area(self):
		return self.height * self.base

triangle = Triangle(3, 5)
print(triangle.area())