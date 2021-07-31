import csv

with open('E:\\Programming\\Literature\\The Self-Taught Programmer\\Ch 9\\t.csv', 'r') as f:
	r = csv.reader(f, delimiter = ',')
	for row in r:
		print(','.join(row))
