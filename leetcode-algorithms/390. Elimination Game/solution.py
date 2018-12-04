def lastRemaining(n):
	"""
	:type n: int
	:rtype: int
	"""
	l = list(range(1,n+1))
	for i,v in enumerate(l):
		if i % 2==1 :
			l.remove(v)
	return l





if __name__ == '__main__':
	res = lastRemaining(9)
	print(res)