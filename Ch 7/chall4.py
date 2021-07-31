numbers = [11, 13, 14, 1, 743, 6, 777, 6662]
x = 0
print("Welcome to Number quesser!\nI have some numbers for ya'...")

while True:
	answer = (input('|||||Type X to quit.|||||\n|||||You have {} points|||||\nTry to guess my numbers:').format(x))
	if answer == 'X':
		print('Quiting...')
		break
	try:
		answer = int(answer)
	except ValueError:
		print('You need to type a number of X to quit!')
	if answer in numbers:
		print('You are right!')
		x += 1
	else:
		print("Let's another number.")
