def rangeBitwiseAnd(m, n):
	"""
	:type m: int
	:type n: int
	:rtype: int
	"""

	i = 0
	while m != n:
		m >>= 1
		n >>= 1
		i += 1
	return m << i



if __name__ == '__main__':
	m = 1
	n = 222222

	res = rangeBitwiseAnd(m,n)
	print(res)