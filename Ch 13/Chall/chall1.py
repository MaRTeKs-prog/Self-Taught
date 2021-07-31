from math import pi

class Circle:
	def __init__(self, r):
		self.radius = r

	def calculate_perimeter(self):
		return 2 * pi * self.radius

class Square:
	def __init__(self, s):
		self.side = s

	def calculate_perimeter(self):
		return self.side * 4

circle = Circle(3)
print(circle.calculate_perimeter())

square = Square(5)
print(square.calculate_perimeter())

# Тут я заметил, что перепутал круг и прямоугольник

class Rectangle:
	def __init__(self, w, l):
		self.width = w
		self.length = l

	def calculate_perimeter(self):
		return (self.width + self.length) * 2

rectangle = Rectangle(2, 3)
print(rectangle.calculate_perimeter())