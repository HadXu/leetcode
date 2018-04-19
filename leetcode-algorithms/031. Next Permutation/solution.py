def nextPermutation(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	

	k = -1
	for i in range(len(nums)-2,-1,-1):
		if nums[i]<nums[i+1]:
			k = i
			break

	if k==-1:
		nums.reverse()
		return

	l = -1

	for i in range(len(nums)-1,k,-1):
		if nums[i]>nums[k]:
			l = i
			break

	nums[l],nums[k] = nums[k],nums[l]

	def Myreverse(nums,l,r):
		while l<r:
			nums[l],nums[r] = nums[r],nums[l]
			l += 1
			r -= 1

	Myreverse(nums,k+1,len(nums)-1)


if __name__ == '__main__':
	nums = [1,3,2]
	nextPermutation(nums)
	print(nums)



