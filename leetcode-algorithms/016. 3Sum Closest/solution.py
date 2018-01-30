def threeSumClosest(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	nums.sort()

	if len(nums)<=3:
		return sum(nums)

	n = len(nums)
	res = 0x7fffffff
	for i in range(0,n-2):
		j = i + 1
		k = n - 1
		while j<k:
			s = nums[i]+nums[j]+nums[k]
			if abs(target-res)>abs(target-s):
				res = s
				if res == target:
					return res
			if s > target:
				k -= 1
			else:
				j += 1
	return res

if __name__ == '__main__':
	nums = [-1,2,1,-4]
	target = 1
	res = threeSumClosest(nums,target)
	print(res)