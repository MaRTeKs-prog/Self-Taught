class PublicPrivateExample:
	def __init__(self):
		self.public = 'safe'
		self._unsafe = 'unsafe'

	def public_method(self):
		# Client can use it
		pass

	def _unsafe_method(self):
		# Client can't use it
		pass
		self.public = 'safe'
		self._unsafe = 'unsafe'

'''
Методы открытые и закрытые отличаются
только визуально (строка 10):
перед закрытыми ставиться
нижнее подчёркивание, которое
сигнализирует о небезопасном для
выполнение программы методе. Так же
и с переменными класса (строка 4).
'''