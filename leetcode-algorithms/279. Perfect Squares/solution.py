def numSquares(n):
	"""
	:type n: int
	:rtype: int
	"""


	if n<=0:
		return 0

	INT_MAX = 0xffffffff
	res = [INT_MAX for _ in range(n+1)]

	res[0] = 0

	for i in range(1,n+1):
		for j in range(1,i+1):
			if j*j <= i:
				res[i] = min(res[i],res[i - j*j]+1)

	return res[-1]




if __name__ == '__main__':
	n = 12

	res = numSquares(n)

	print(res)
