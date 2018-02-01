# 4Sum

该题目属于比较难一种，由于前面有3sum的经验，这题不是特别的难。

**首先固定一个数，不就是求解3sum的问题了嘛！**

**在次固定一个数，不就是求2sum的问题了嘛！**

```python
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
```



在使用Python求解该问题的时候，算法思路与C++一样，但是一直出现重复的数。。。。

算了，我就曲线救国，用tuple+set，最后转list，一样的。




