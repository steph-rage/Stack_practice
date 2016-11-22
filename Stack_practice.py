class Stack:
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.array = [None] * self.capacity

	def is_empty(self):
		return True if self.top == -1 else False

	def add(self, next):
		try:
			self.array[self.top + 1] = next
			self.top += 1
		except IndexError:
			self.place_holder = self.array
			self.array = [None] * 2 * self.capacity
			for i in range(self.capacity):
				self.array[i] = self.place_holder[i]
			self.capacity = 2 * self.capacity
			self.add(next)

	def remove(self):
		try: 
			self.array[self.top] = None
			self.top -= 1 
		except IndexError:
			pass

	def peek(self):
		return self.array[self.top]


def reverse(word):
	word_stack = Stack(10)
	reverse_stack = Stack(10)

	for letter in word:
		word_stack.add(letter)
	
	while not word_stack.is_empty():
		print(word_stack.peek(), end = "")
		word_stack.remove()

	print("")



new_word = input("Type any word to reverse: ")

reverse(new_word)

