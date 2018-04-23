def lengthOfLastWord(s):
	"""
	:type s: str
	:rtype: int
	"""
	s = s.strip()
	i = len(s) - 1
	res = 0
	while i>=0 and s[i]!=' ':
		i -= 1
		res += 1
	return res

		



if __name__ == '__main__':
	s = 'hello world'
	res = lengthOfLastWord(s)
	print(res)

