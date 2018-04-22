def myPow(x, n):
	"""
	:type x: float
	:type n: int
	:rtype: float
	"""

	# 0 表示正数或0  
	# 1 表示负数
	if n<0:
		x = 1./x
		n = -n
	pow = 1
	while n:
		if n&1:
			pow *= x
		x *= x
		n >>= 1
	return pow



if __name__ == '__main__':
	x = 2.
	y = 10

	res = myPow(x,y)

	print(res)