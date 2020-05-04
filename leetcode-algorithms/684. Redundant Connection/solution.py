from typing import List


class DSU:
	def __init__(self, p):
		self.p = list(range(p))
	def find(self, x):
		if self.p[x] != x:
			self.p[x] = self.find(self.p[x])
		return self.p[x]
	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		self.p[x] = y




class Solution:
	def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
		dsu = DSU(2001)
		for u,v in edges:
			if dsu.find(u) == dsu.find(v):
				return [u,v]
			dsu.union(u, v)
		return []





if __name__ == '__main__':
	edges = [[1,2], [1,3], [2,3]]
	res = Solution().findRedundantConnection(edges)
	print(res)


