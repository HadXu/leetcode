def removeDuplicates(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if not nums:
		return 0
	res = 1
	for i in range(1, len(nums)):
		if nums[i] != nums[i-1]:
			nums[res] = nums[i]
			res += 1
	return res

if __name__ == '__main__':
	nums = [1, 1, 2]
	res = removeDuplicates(nums)
	print(res,nums)
        