class Horse:
	def __init__(self, name, rider):
		self.rider = rider
		self.name = name

class Rider:
	def __init__(self, name):
		self.name = name

mike = Rider('Mike')
jade = Horse('Jade', mike)

print(jade.rider.name)