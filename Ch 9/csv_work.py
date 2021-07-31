import csv

with open('E:\\Programming\\Literature\\The Self-Taught Programmer\\Ch 9\\t.csv', 'w') as f:
	w = csv.writer(f, delimiter = ',')
	w.writerow(['один', 'два', 'три'])
	w.writerow(['четыре', 'пять', 'шесть'])
