def compress(chars):
	"""
	:type chars: List[str]
	:rtype: int
	"""
	from itertools import groupby

	res = [(k+str(len(list(v)))) for k,v in groupby(chars)]

	return len(''.join(res))






if __name__ == '__main__':
	chars = ["a","a","b","b","c","c","c","c","c",'c','c','c','c','c','c']

	res = compress(chars)
	print(res)