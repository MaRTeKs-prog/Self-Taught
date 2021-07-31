class Person:
	def __init__(self):
		self.name = 'Боб'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

# В этой версии Python это свойство работает по другому!
# Если в 5 и 9 строке добавить скобки (Person()), то всё работает, как в книге!
# Возможно, со скобками оно считает его, как за другой экземпляр класса?
# То есть, до этого они были одинаковыми? (До этого, я особо скобки не ставил)