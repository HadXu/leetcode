def minimumTotal(triangle):
	"""
	:type triangle: List[List[int]]
	:rtype: int
	"""
	res = triangle[-1]

	for layer in range(len(triangle)-2,-1,-1):
		for i in range(0,layer+1):
			res[i] = min(res[i],res[i+1])+triangle[layer][i]


	return res[0]





if __name__ == '__main__':
	triangle = [
			     [2],
			    [3,4],
			   [6,5,7],
			  [4,1,8,3]
			]

	res = minimumTotal(triangle)

	print(res)