me = {
	'Game': 'The Binding of Isaac',
	'Book': 'State',
	'Color': 'Purple'
}

me['Track'] = 'Expurgation'

""" print(me)
print(me['Book']) """

answer = input("Ask something about me:")
if answer in me:
	print(me[answer])

