a = int(input("Type a number:"))
b = int(input("Type another number:"))

try:
	print(a / b)
except ZeroDivisionError:
	print("You can't divide by zero!")
