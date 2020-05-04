def solution(matrix):

	n = len(matrix[0])
	heights = [0] * n

	area = 0

	for row in matrix:
		for i in range(n):
			if row[i] == '1':
				heights[i] += 1
			else:
				heights[i] = 0

		print(heights)
		tmp = maxArea(heights)
		area = max(tmp, area)

	return area



def maxArea(heights):
	stack = []
	area = 0
	index = 0
	while index < len(heights):
		if (not stack) or (heights[stack[-1]] < heights[index]):
			stack.append(index)
			index += 1
		else:
			tp = stack.pop()
			temp = heights[tp] * ((index-1-stack[-1]) if stack else index)
			area = max(area, temp)

	while stack:
		tp = stack.pop()
		temp = heights[tp] * ((index-1-stack[-1]) if stack else index)
		area = max(area, temp)

	return area

if __name__ == '__main__':
	matrix = [
			["1","0","1","0","0"],
			["1","0","1","1","1"],
			["1","1","1","1","1"],
			["1","0","0","1","0"]]

	res = solution(matrix)
	print(res)