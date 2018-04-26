def mostCommonWord(paragraph, banned):
	"""
	:type paragraph: str
	:type banned: List[str]
	:rtype: str
	"""
	import re
	from collections import Counter

	words = paragraph.lower()
	words = re.findall(r'\w+',words)

	c = Counter(words).most_common()

	res = [k[0] for k in c if k[0] not in banned][0]

	return res







if __name__ == '__main__':
	paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
	banned = ["hit"]
	res = mostCommonWord(paragraph,banned)

	print(res)