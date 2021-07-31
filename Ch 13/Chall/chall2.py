class Square:
	def __init__(self, s):
		self.side = s

	def change_size(self, x):
		self.side += x

	def calculate_perimeter(self):
		return self.side * 4

square = Square(2)
print(square.calculate_perimeter())
square.change_size(3)
print(square.calculate_perimeter())

