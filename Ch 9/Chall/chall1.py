st = open('E:\\Programming\\Literature\\The Self-Taught Programmer\\Ch 9\\csv.txt', 'r')
print(st.read())
st.close()

with open('E:\\Programming\\Literature\\The Self-Taught Programmer\\Ch 9\\csv.txt', 'r') as f:
	print(f.read())

# He has some troubles with reading of Russian texts