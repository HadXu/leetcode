def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[-1]

if __name__ == '__main__':
    nums = [3,3,7,7,10,11,11]
    res = singleNonDuplicate(nums)
    print(res)
