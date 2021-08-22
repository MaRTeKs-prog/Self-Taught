def palidrom(word):
	word = word.lower()
	return word[::-1] == word

print(palidrom('Мама'))
print(palidrom('Мам'))