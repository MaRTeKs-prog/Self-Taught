try:
	a = int(input("Type a number:"))
	b = int(input("Type another number:"))
	print(a / b)
except (ZeroDivisionError, ValueError):
	print("Type error!")
