def isPerfectSquare(num):
	"""
	:type num: int
	:rtype: bool
	"""

	i = 1
	while num>0:
		num -= i
		i += 2
	return num == 0




if __name__ == '__main__':
	
	num = 16
	print(isPerfectSquare(num))