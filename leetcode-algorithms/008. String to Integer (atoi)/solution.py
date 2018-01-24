def myAtoi(str):
	ans = 0
	maxint = 0x7fffffff
	minint = -2147483648
	maxVal = 0x100000000

	flag = False

	st = 0

	while st<len(str) and str[st]==' ':
		st += 1
	if st<len(str) and str[st]=='+':
		st += 1
	else:
		if st<len(str) and str[st]=='-':
			flag = True
			st += 1
	for i in range(st,len(str)):
		if str[i]<='9' and str[i]>='0':
			ans = ans * 10 + int(str[i])
			if ans>maxVal:
				ans = maxVal
		else:
			break

	if flag:
		ans = -ans

	if ans > maxint:
		ans = maxint
	if ans < minint:
		ans = minint

	return ans

if __name__ == '__main__':
	s = '234'
	res = myAtoi(s)

	print(res)