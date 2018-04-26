def selfDividingNumbers(left, right):
	"""
	:type left: int
	:type right: int
	:rtype: List[int]
	"""
	res = []

	for i in range(left,right+1):

		local = i
		flag = True

		while local:
			rem = local % 10
			local //= 10

			if rem == 0:
				flag = False
				break
			if i%rem != 0:
				flag = False
		if flag:
			res.append(i)

	return res


if __name__ == '__main__':
	left = 1
	right = 22

	res = selfDividingNumbers(left,right)
	print(res)
