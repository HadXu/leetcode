def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_len = i = 0
    while i < len(nums):
        curr = 1
        while i + 1 < len(nums) and nums[i] < nums[i + 1]:
            curr, i = curr + 1, i + 1
        max_len = max(curr, max_len)
        i += 1
    return max_len


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    res = findLengthOfLCIS(nums)
    print(res)
