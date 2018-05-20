def findNthDigit(n):
	"""
	:type n: int
	:rtype: int
	"""
	

	s = map(str,range(1,n+1))
	res = ''.join(''.join(s))

	return str(res[n-1])

if __name__ == '__main__':
	n = 100000000
	res = findNthDigit(n)
	print(res)


