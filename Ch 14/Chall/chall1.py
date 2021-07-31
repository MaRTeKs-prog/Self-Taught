class Square:
	square_list = []

	def __init__(self, b):
		self.base = b
		self.square_list.append(self)

s1 = Square(1)
s2 = Square(3)
s3 = Square(12)

print(Square.square_list)