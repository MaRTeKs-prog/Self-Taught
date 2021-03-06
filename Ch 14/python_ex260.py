class Rectangle:
	recs = []

	def __init__(self, w, l):
		self.width = w
		self.len = l
		self.recs.append((self.width, self.len)) # Здесь укзан кортеж, но может быть список или словарь

	def print_size(self):
		print('''{} на {}
		'''.format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)