from typing import List

class Solution:
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		
		def infect(grid, i, j):
			if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
				return 0
			grid[i][j] = -1

			return 1+infect(grid,i,j+1)+infect(grid,i,j-1)+infect(grid,i+1,j)+infect(grid,i-1,j)

		res = -1
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					cur = infect(grid, i, j)

					res = max(res, cur)
		return res

if __name__ == '__main__':
	grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
			 [0,0,0,0,0,0,0,1,1,1,0,0,0],
			 [0,1,1,0,1,0,0,0,0,0,0,0,0],
			 [0,1,0,0,1,1,0,0,1,0,1,0,0],
			 [0,1,0,0,1,1,0,0,1,1,1,0,0],
			 [0,0,0,0,0,0,0,0,0,0,1,0,0],
			 [0,0,0,0,0,0,0,1,1,1,0,0,0],
			 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
	res = Solution().maxAreaOfIsland(grid)
	print(res)