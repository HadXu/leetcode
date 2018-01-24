class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i,v in enumerate(nums):
        	if (target - v) not in res:
        		res[v] = i;
        	else:
        		return [res[target-v],i]


if __name__ == '__main__':
	s = Solution()
	nums = [2,7,11,15]
	target = 9
	print(s.twoSum(nums,target))

