def strStr(haystack, needle):
	"""
	:type haystack: str
	:type needle: str
	:rtype: int
	"""

	for i in range(len(haystack)+1):
		for j in range(len(needle)+1):
			print(i,j)
			if j==len(needle):
				return i
			if i+j == len(haystack):
				return -1
			if needle[j] != haystack[i+j]:
				break

if __name__ == '__main__':
	haystack = 'aaaaa'
	needle = 'bba'
	res = strStr(haystack,needle)
	print(res)