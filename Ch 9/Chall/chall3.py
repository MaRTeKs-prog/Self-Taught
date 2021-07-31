import csv

my_list = [['Звездные войны', 'Терминатор', 'Искусственный интеллект'], ['Люди в чёрном', 'Я - робот', 'Эволюция']]
with open('E:\\Programming\\Literature\\The Self-Taught Programmer\\Ch 9\\Chall\\chall3.csv', 'w') as f:
	w = csv.writer(f, delimiter = ',')
	w.writerow(my_list[0])
	w.writerow(my_list[1])

