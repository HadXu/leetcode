class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        return random.choice([k for k,v in enumerate(self.nums) if v==target])


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3]
    target = 3
    obj = Solution(nums)
    param_1 = obj.pick(target)
    print(param_1)
