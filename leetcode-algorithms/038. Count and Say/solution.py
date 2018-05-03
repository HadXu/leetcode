def countAndSay(n):
	"""
	:type n: int
	:rtype: str
	"""

	from itertools import groupby

	s = '1'
	for _ in range(n-1):
		s = groupby(s)
		res = [str((len(list(v))))+k for k,v in s]
		s = ''.join(res)
	return s



if __name__ == '__main__':
	n = 10
	print(countAndSay(n))
