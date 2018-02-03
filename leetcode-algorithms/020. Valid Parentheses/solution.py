def isValid(s):
	"""
	:type s: str
	:rtype: bool
	"""

	if not s:
		return True

	satck = []

	k_v = {')':'(',']':'[','}':'{'}

	for c in s:
		if c in k_v.values():
			satck.append(c)
			continue
		if satck and k_v[c] == satck[-1]:
			satck.pop()
		else:
			return False

	return  not satck




if __name__ == '__main__':
	s=']'
	res = isValid(s)
	print(res)


