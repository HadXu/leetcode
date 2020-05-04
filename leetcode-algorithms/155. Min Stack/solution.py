class MinStack:

	def __init__(self):
		self.l = []

	def push(self, x: int) -> None:
		if not self.l or x <= self.l[-1][1]:
			self.l.append((x, x))

		if x > self.l[-1][1]:
			self.l.append((x, self.l[-1][1]))


	def pop(self) -> None:
		if self.l:
			self.l.pop()



	def top(self) -> int:
		if self.l:
			return self.l[-1][0]


	def getMin(self) -> int:
		if self.l:
			return self.l[-1][1]

if __name__ == '__main__':
	obj = MinStack()
	obj.push(2)
	obj.push(0)
	obj.push(3)
	obj.push(0)
	# obj.pop()
	param_3 = obj.top()
	param_4 = obj.getMin()

	print(obj.l)
	print(param_3)
	print(param_4)

