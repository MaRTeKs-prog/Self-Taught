class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		last = len(self.items) - 1
		return self.items[last]

	def size(self):
		return len(self.items)

stack = Stack()
list = [1, 2, 3, 4, 5]

for i in list:
	stack.push(i)

reverse_list = []

for i in range(len(stack.items)):
	reverse_list.append(stack.pop())

print(reverse_list)