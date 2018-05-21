def numTrees(n):
	"""
	:type n: int
	:rtype: int
	"""


	res = [0 for _ in range(n+1)]
	res[0] = res[1] = 1

	for i in range(2,n+1):
		for j in range(1,i+1):
			res[i] += res[j-1]*res[i-j]
	return res[n]


if __name__ == '__main__':
	n = 3
	res = numTrees(n)

	print(res)