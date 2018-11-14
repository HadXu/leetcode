def setZeroes(matrix):
	"""
	:type matrix: List[List[int]]
	:rtype: void Do not return anything, modify matrix in-place instead.
	"""
	row = False
	col = False
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				if i == 0:
					row = True
				if j == 0:
					col = True
				matrix[i][0] = matrix[0][j] = 0
	for i in range(1,len(matrix)):
		for j in range(1,len(matrix[0])):
			if matrix[i][0] == 0 or matrix[0][j] == 0:
				matrix[i][j] = 0

	if col:
		for i in range(len(matrix)):
			matrix[i][0] = 0

	if row:
		for i in range(len(matrix[0])):
			matrix[0][i] = 0

	






if __name__ == '__main__':
	matrix = [
	  [1,1,1],
	  [1,0,1],
	  [1,1,1]
	]
	setZeroes(matrix)

	print(matrix)