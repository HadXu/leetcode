def reverseOnlyLetters(S):
	"""
	:type S: str
	:rtype: str
	"""
	res = ''
	chars = [c for c in S if c.isalpha()][::-1]
	j = 0
	for i in range(len(S)):
		if S[i].isalpha():
			res += chars[j]
			j += 1
		else:
			res += S[i]
	return res

if __name__ == '__main__':
	S = 'Test1ng-Leet=code-Q!'
	res = reverseOnlyLetters(S)
	print(res)