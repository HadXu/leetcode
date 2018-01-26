def intToRoman(num):
	"""
	:type num: int
	:rtype: str
	"""
	values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
	symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
	res = ''
	assert len(values) == len(symbols)

	i = 0
	while num>0:
		k,_ = divmod(num,values[i])
		for _ in range(k):
			res += symbols[i]
			num -= values[i]
		i += 1

	return res

if __name__ == '__main__':
	res = intToRoman(3999)
	print(res)
