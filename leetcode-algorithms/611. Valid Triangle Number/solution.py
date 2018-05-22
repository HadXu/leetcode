def triangleNumber(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""

	nums.sort()

	print(nums)

	res = 0

	for i in range(2,len(nums)):
		l = 0
		r = i - 1
		while l<r:
			if nums[l]+nums[r]>nums[i]:
				res += r - l
				r -= 1
			else:
				l += 1
	return res




if __name__ == '__main__':
	nums = [2,2,3,4]
	res = triangleNumber(nums)
	print(res)
