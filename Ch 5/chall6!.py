''' About multiplicity (I think, this name is not correct)
https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html
Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.
'''

m = set('hello')
print(m)

m = set(i ** 2 for i in range(10)) # Генератор множества (???)
print(m)

print(type(m))

words = ['hello', 'daddy', 'hello', 'mum'] # Список
print(set(words))
