def combinationSum3(k, n):
	"""
	:type k: int
	:type n: int
	:rtype: List[List[int]]
	"""
	from itertools import combinations

	return [c for c in combinations(range(1,10),k) if sum(c)==n]



if __name__ == '__main__':
	
	k = 3
	n = 9
	res = combinationSum3(k,n)
	print(res)