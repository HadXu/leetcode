def divide(dividend, divisor):
	"""
	:type dividend: int
	:type divisor: int
	:rtype: int
	"""
	if not divisor or (dividend== -2147483648 and divisor==-1):
		return 2147483647
	sign = -1 if ((dividend<0)^(divisor<0)) else 1
	dvd = abs(dividend)
	dvs = abs(divisor)
	res = 0
	while dvd>=dvs:
		tmp = dvs
		multiple = 1
		while dvd>=(tmp<<1):
			tmp <<= 1
			multiple <<= 1
		dvd -= tmp
		res += multiple
	return res if sign==1 else -res

if __name__ == '__main__':
	dividend = 15
	divisor =3
	res = divide(dividend, divisor)
	print(res)


	print(2<<30)


