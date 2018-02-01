def fourSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[List[int]]
	"""
	res =[]
	if len(nums)<4:
		return res

	nums = sorted(nums)

	for i in range(0,len(nums)):
		target_3 = target - nums[i]
		for j in range(i+1,len(nums)):
			target_2 = target_3 - nums[j]

			front = j + 1
			back = len(nums) - 1

			while front<back:
				two_sum = nums[front]+nums[back]

				if two_sum < target_2:
					front += 1
				elif two_sum > target_2:
					back -= 1
				else:
					tmp = (nums[i],nums[j],nums[front],nums[back])
					res.append(tmp)
					while (front<back and nums[front]==tmp[2]):
						front += 1
					while front<back and nums[back] == tmp[3]:
						back -= 1
			while j+1<len(nums) and nums[j+1] == nums[j]:
				j += 1
		while i+1 < len(nums) and nums[i+1] == nums[i]:
			i += 1
	return list(set(res))




if __name__ == '__main__':
	nums = [-3,-2,-1,0,0,1,2,3]
	target = 0
	res = fourSum(nums, target)
	print(res)
