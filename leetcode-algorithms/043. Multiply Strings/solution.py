def multiply(num1, num2):
	"""
	:type num1: str
	:type num2: str
	:rtype: str
	"""
	
	l = len(num1) + len(num2)
	res = [0]*l


	for i in range(len(num1)-1,-1,-1):
		for j in range(len(num2)-1,-1,-1):
			k = int(num1[i]) * int(num2[j])
			p1, p2 = i+j, i+j+1

			s = k + res[p2]

			res[p1] += s // 10
			res[p2] = s % 10

	s = ''

	for i in res:
		if not (i ==0 and len(s)==0):
			s += str(i)

	return s if len(s)!=0 else '0'




if __name__ == '__main__':
	res = multiply('123','45')
	print(res)