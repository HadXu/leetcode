class DSU:
	def __init__(self, N):
		self.p = list(range(N))

	def find(self, x):
		if self.p[x] != x:
			self.p[x] = self.find(self.p[x])
		return self.p[x]

	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		self.p[x] = y

