def lexicalOrder(n):
	"""
	:type n: int
	:rtype: List[int]
	"""
	res = []
	curr = 1
	for i in range(1,n + 1):
		res.append(curr)
		if curr * 10 <= n:
			curr *= 10
		elif (curr % 10 != 9) & (curr + 1 <= n):
			curr += 1
		else:
			while (curr // 10) % 10 == 9:
				curr //= 10
			curr = curr // 10 + 1
	return res



if __name__ == '__main__':
	res = lexicalOrder(500)
	print(res)