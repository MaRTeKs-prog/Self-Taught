class Shape:
	def what_am_i(self):
		print('Я - фигура!')

class Rectangle(Shape):
	def __init__(self, w, l):
		self.width = w
		self.length = l

	def calculate_perimeter(self):
		return (self.width + self.length) * 2

class Square(Shape):
	def __init__(self, s):
		self.side = s

	def calculate_perimeter(self):
		return self.side * 4

square = Square(5)
rectangle = Rectangle(6, 4)
square.what_am_i()
rectangle.what_am_i()