def isMonotonic(A):
	"""
	:type A: List[int]
	:rtype: bool
	"""
	def cmp(x,y):
		if x>y:
			return 1
		if x < y:
		    return -1
		return 0

	return not {cmp(i, j) for i, j in zip(A, A[1:])} >= {1, -1}


if __name__ == '__main__':
	A = [1,2,2,3]
	print(isMonotonic(A))