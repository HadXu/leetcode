def reverse(x):
	"""
	:type x: int
	:rtype: int
	"""

	if x < 0:
		res = -1 * int(str(-x)[::-1])
	else:
		res = int(str(x)[::-1])
	if abs(res) > 0x7fffffff:
		return 0
	return res


if __name__ == '__main__':
	x = 1563847412
	print(reverse(x))

