def judgeSquareSum(c):
	"""
	:type c: int
	:rtype: bool
	"""

	s = set()
	for i in range(0,int(c**0.5)+1):
		s.add(i*i)
		if c-i*i in s:
			return True
	return False




if __name__ == '__main__':
	c = 1
	res = judgeSquareSum(c)
	print(res)