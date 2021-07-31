# О наследовании от класс Object

class Lion:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

lion = Lion("Gaus")
print(lion)


class Lion1:
	def __init__(self, name):
		self.name = name

lion1 = Lion1("Mag")
print(lion1)