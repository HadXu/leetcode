def calculate(s):
	"""
	:type s: str
	:rtype: int
	"""
	digis = '0123456789'

	stack = []
	result = 0
	number = 0
	sign = 1
	for c in s:
		if c in digis:
			number = number * 10 + ord(c) - ord('0')
		elif c == '+':
			result += sign * number
			number = 0
			sign = 1
		elif c == '-':
			result += sign * number
			number = 0
			sign = -1

		elif c == '(':
			stack.append(result)
			stack.append(sign)
			sign = 1
			result = 0
		elif c == ')':
			result += sign * number
			number = 0
			result *= stack.pop()
			result += stack.pop()

	if number !=0 :
		result += sign * number



	return result

if __name__ == '__main__':
	s = '(1+(4+5+2)-3)+(6+8)'
	res = calculate(s)
	print(res)