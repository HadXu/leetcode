def isPalindrome(x):
	"""
	:type x: int
	:rtype: bool
	"""

	x = str(x)

	if x != x[::-1]:
		return False
	return True





if __name__ == '__main__':
	x = 12321
	res = isPalindrome(x)
	print(res)

