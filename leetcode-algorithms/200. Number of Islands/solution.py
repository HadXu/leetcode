from typing import List

class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if not grid:
			return 0
		r, c = len(grid), len(grid[0])
		res = 0
		visited = [[False for _ in range(c)] for _ in range(r)]

		def dfs(i, j):
			if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0' or visited[i][j]:
				return
			visited[i][j] = True

			for x, y in [(-1,0),(0,-1),(1,0),(0,1)]:
				dfs(i+x, j+y)

			# dfs(i, j+1)
			# dfs(i, j-1)
			# dfs(i+1, j)
			# dfs(i-1, j)

		for i in range(r):
			for j in range(c):
				if not visited[i][j] and grid[i][j] == '1':
					dfs(i, j)
					res += 1
		return res



if __name__ == '__main__':
	grid = [[x for x in '11110'],[x for x in '11010'], [x for x in '11000'], [x for x in '00000']]
	res = Solution().numIslands(grid)
	print(res)