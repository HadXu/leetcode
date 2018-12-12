def countSmaller(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	x = []
	for i,p in enumerate(nums):
		x.append([t for t in nums[i:] if t < p])

	return [len(s) for s in x]





if __name__ == '__main__':
	nums = [5,2,6,1]
	res = countSmaller(nums)
	print(res)