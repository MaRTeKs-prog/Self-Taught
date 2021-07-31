# Не хочу писать документацию. Это скучно.

def sqrd():
	''' Возводит целое число в квадрат
	:переменная x: целое число
	:print(x): отображение(!!!) результата
	'''
	x = int(input())
	print(x**2)

sqrd()


def string(x):
	print(x)

string("Hello there!")


def example(x, y, z, a=2, b=1):
	print((x + y + z) ** a * b)

example(2, 3, 1)
example(2, 3, 1, 3, 2)


def d2(x):
	return x / 2

def d4(x):
	return x * 4

x = d2(32)
y = d4(x)

print(y)


def flt(x):
	try:
		y = float(x)
		print(y)
	except ValueError:
		print('You need to write a number!')

flt('Hello there!')
"""
print(flt(6))
If line 4 == return y
"""
flt('6')
