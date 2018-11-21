def maxProduct(words):
	"""
	:type words: List[str]
	:rtype: int
	"""
	# l = len(words)
	# res = 0
	# for i in range(0,l-1):
	# 	i_chars = set(words[i])
	# 	for j in range(i+1,l):
	# 		j_chars = set(words[j])
	# 		if not (i_chars & j_chars):
	# 			res = max(res, len(words[i]) * len(words[j]))

	# return res

	res = 0
	cheaker = []
	l = len(words)
	for word in words:
		num = 0
		for c in word:
			num  |= 1<<(ord(c) - ord('a'))
		cheaker.append(num)



	for i in range(0,l-1):
		for j in range(i,l):
			if (cheaker[i] & cheaker[j]) == 0:
				res = max(res, len(words[i]) * len(words[j]))

	return res



if __name__ == '__main__':
	words = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]
	res = maxProduct(words)

	print(res)