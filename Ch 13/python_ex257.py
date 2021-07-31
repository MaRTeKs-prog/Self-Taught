class Dog:
	def __init__(self,
				name,
				breed,
				owner):
		self.name = name
		self.breed = breed
		self.owner = owner

class Person:
	def __init__(self, name):
		self.name = name

sasha = Person('Cаша')
kyza = Dog('Кузя',
			'Йоркшерский терьер',
			sasha)
print(kyza.owner.name)
