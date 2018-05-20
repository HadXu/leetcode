def minPathSum(grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""

	m = len(grid)
	n = len(grid[0])

	sum = [[grid[0][0] for _ in range(n)] for _ in range(m)]

	for i in range(1,m):
		sum[i][0] = sum[i-1][0]+grid[i][0]

	for i in range(1,n):
		sum[0][i] = sum[0][i-1] + grid[0][i]


	for i in range(1,m):
		for j in range(1,n):
			sum[i][j] = min(sum[i-1][j],sum[i][j-1])+grid[i][j]


	return sum[m-1][n-1]




if __name__ == '__main__':
	grid = [
	  [1,3,1],
	  [1,5,1],
	  [4,2,1]
	]

	res = minPathSum(grid)

	print(res)







