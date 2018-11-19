def toGoatLatin(S):
	"""
	:type S: str
	:rtype: str
	"""
	vowel = {'a','e','i','o','u'}

	res = ''
	words = S.split()
	for i, w in enumerate(words,1):
		if w.lower()[0] in vowel:
			res += w+'ma'+'a' * i
		if w.lower()[0] not in vowel:
			temp = w[1:]+w[0]+'ma' + 'a' * i
			res += temp
		if i != len(words):
			res += ' '

	return res

if __name__ == '__main__':
	S = "The quick brown fox jumped over the lazy dog"

	S = toGoatLatin(S)

	print(S)




