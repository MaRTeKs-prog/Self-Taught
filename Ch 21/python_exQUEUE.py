# Ex. 295

class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item) # Здесь код работает не как в книге

	def dequeue(self, item):
		self.items.pop()

	def size(self):
		return len(self.items)

# Ex. 296-298

a_queue = Queue()
print(a_queue.size())

for i in range(5):
	a_queue.enqueue(i)

print(a_queue.size())

for i in range(5):
	a_queue.dequeue(i)

print()
print(a_queue.size())
