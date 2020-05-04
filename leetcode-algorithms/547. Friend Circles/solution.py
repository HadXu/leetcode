from typing import List
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


class Solution:
	def findCircleNum(self, M: List[List[int]]) -> int:
		
		def dfs(node):
			for nei, adj in enumerate(M[node]):
				if adj and nei not in seen:
					seen.add(nei)
					dfs(nei)

		N = len(M)
		seen = set()
		ans = 0
		for i in range(N):
			if i not in seen:
				dfs(i)
				ans += 1
		return ans


	def findCircleNum2(self, M: List[List[int]]) -> int:
		dsu = DSU(len(M))

		for i in range(len(M)):
			for j in range(len(M)):
				if M[i][j] == 1:
					dsu.union(i, j)


		return sum(dsu.find(x)==x for x in range(len(M)))



if __name__ == '__main__':
	M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
	res = Solution().findCircleNum2(M)
	print(res)









