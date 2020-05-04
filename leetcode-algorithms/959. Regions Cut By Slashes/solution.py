from typing import List
class DSU:
	def __init__(self, N):
		self.p = list(range(N))

	def find(self, x):
		if self.p[x] != x:
			self.p[x] = self.find(self.p[x])
		return self.p[x]

	def union(self, p, q):
		p = self.find(p)
		q = self.find(q)
		self.p[p] = q

class Solution:
	def regionsBySlashes(self, grid: List[str]) -> int:
		N = len(grid)
		dsu = DSU(4 * N * N)

		for r, row in enumerate(grid):
			for c, val in enumerate(row):
				root = 4 * (r*N + c)
				print('r',r,'c',c)

				if val in '/ ':
					dsu.union(root + 0, root + 1)
					dsu.union(root + 2, root + 3)


				if val in '\\ ':
					dsu.union(root + 0, root + 2)
					dsu.union(root + 1, root + 3)


				if r+1 < N: dsu.union(root + 3, (root+4*N) + 0)
				if r-1 >= 0: dsu.union(root + 0, (root-4*N) + 3)
				if c+1 < N: dsu.union(root + 2, (root+4) + 1)
				if c-1 >= 0: dsu.union(root + 1, (root-4) + 2)



		return sum(dsu.find(x) == x for x in range(4*N*N))

if __name__ == '__main__':
	grid = ["//", "/ "]
	res = Solution().regionsBySlashes(grid)
	print(res)


		