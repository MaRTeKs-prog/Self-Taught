# Ex. 289

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

# Ex. 290 - 293

stack1 = Stack()
stack1.push(1)
print(stack1.is_empty())
item = stack1.pop()
print(item)
print(stack1.is_empty())

for i in range(0, 6):
	stack1.push(i)

print(stack1.peek())
print(stack1.size())

# Ex. 294

stack2 = Stack()
for i in 'Привет':
	stack2.push(i)

reverse = ""
print(stack2.items)

for i in range(len(stack2.items)):
	reverse += stack2.pop()

print(reverse)
print(stack2.items)