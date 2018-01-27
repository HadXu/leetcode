def romanToInt(s):
	"""
	:type s: str
	:rtype: int
	"""
	c2v = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	prev = 0
	res = 0
	for c in s:
		curr = c2v.get(c)
		res += (curr-2*prev) if (curr>prev) else curr
		prev = curr
	return res



if __name__ == '__main__':
	s = 'MMMCMXCIX'
	res = romanToInt(s)
	print(res)