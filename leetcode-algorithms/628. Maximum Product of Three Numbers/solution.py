def maximumProduct(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	nums.sort()

	return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    

if __name__ == '__main__':
	nums = [-4,-3,-2,-1,60]
	res = maximumProduct(nums)

	print(res)


