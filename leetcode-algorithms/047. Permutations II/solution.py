def permuteUnique(nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""

	def dfs(nums,used,x,res):
		if len(x) == len(nums):
			res.append(x)
			return
		for i in range(len(nums)):
			if used[i]:
				continue
			if i > 0 and nums[i-1]==nums[i] and not used[i-1]:
				continue
			used[i]=True;
			x.append(nums[i])
			dfs(nums,used,x,res)
			used[i] = False
			del x[-1]

	res = []
	x = []
	if len(nums) == 0:
		return res
	used = [True] * len(nums)
	nums.sort()
	dfs(nums,used,x,res)
	return res


if __name__ == '__main__':
	nums = [1,1,2]
	res = permuteUnique(nums)
	print(res)