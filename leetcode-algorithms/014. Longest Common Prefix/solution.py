def longestCommonPrefix(strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""

	if len(strs) == 0:
		return []

	strs = sorted(strs)

	res = ''

	for i in range(min(len(strs[0]),len(strs[-1]))):
		if strs[0][i] != strs[-1][i]:
			break
		res += strs[0][i]

	return res

if __name__ == '__main__':
	strs = ['123','12','2']
	res = longestCommonPrefix(strs)
	print(res)