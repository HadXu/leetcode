def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    return sum([min(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)])


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    res = arrayPairSum(nums)
    print(res)
