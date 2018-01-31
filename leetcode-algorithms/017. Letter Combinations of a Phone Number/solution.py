def letterCombinations(digits):
	"""
	:type digits: str
	:rtype: List[str]
	"""
	if not digits:
            return []
	num2abc = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
				'7':'pqrs','8':'tuv','9':'wxyz'}

	from itertools import product

	res = []
	for d in digits:
		res.append(num2abc[d])

	return [''.join(l) for l in product(*res)]

if __name__ == '__main__':
	digits = '23'
	res = letterCombinations(digits)
	print(res)
