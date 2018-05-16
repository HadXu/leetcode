def largeGroupPositions(S):
	"""
	:type S: str
	:rtype: List[List[int]]
	"""

	i  = 0
	res = []
	while i<len(S):
		j = i + 1
		while j<len(S) and S[j]==S[i]:
			j += 1
		if (j - i) > 2:
			res.append([i,j-1])
		i = j
	return res








if __name__ == '__main__':
	s = 'abcdddeeeeaabbbcd'
	res = largeGroupPositions(s)
	print(res)

