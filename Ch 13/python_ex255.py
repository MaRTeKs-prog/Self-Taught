class Shape:
	def __init__(self, l, w):
		self.width = w
		self.len = l

	def print_size(self):
		print('{} на {}'.format(self.width, self.len))

class Square(Shape):
	def area(self):
		return self.width * self.len

	def print_size(self):
		print('Я {} на {}'.format(self.width, self.len))

a_square = Square(20, 20)
a_square.print_size()
print(a_square.area())