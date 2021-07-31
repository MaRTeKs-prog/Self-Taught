class RightHexagon:
	def __init__(self, s):
		self.side = s

	def calculate_perimeter(self):
		return self.side * 6

hexagonR = RightHexagon(3)
print(hexagonR.calculate_perimeter())

class Hexagon:
	def __init__(self, s1, s2, s3, s4, s5, s6):
		self.side1 = s1
		self.side2 = s2
		self.side3 = s3
		self.side4 = s4
		self.side5 = s5
		self.side6 = s6

	def calculate_perimeter(self):
		return self.side1 + self.side2 + self.side3 \
			+ self.side4 + self.side5 + self.side6

hexagon = Hexagon(2, 10, 5, 6, 4, 1)
print(hexagon.calculate_perimeter())