from typing import List
class Solution:
	def uniquePathsIII(self, grid: List[List[int]]) -> int:
		self.res = 0

		m, n,empty = len(grid), len(grid[0]),1
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1: x,y = (i, j)
				elif grid[i][j] == 2: end = (i, j)
				elif grid[i][j] == 0: empty += 1

		def dfs(x, y, empty):
			if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0): return
			if (x, y) == end:
				self.res += empty == 0
				return

			grid[x][y] = -4
			dfs(x + 1, y, empty - 1)
			dfs(x - 1, y, empty - 1)
			dfs(x, y + 1, empty - 1)
			dfs(x, y - 1, empty - 1)
			grid[x][y] = 0
		dfs(x,y, empty)
		return self.res




if __name__ == '__main__':
	grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
	res = Solution().uniquePathsIII(grid)

	print(res)


