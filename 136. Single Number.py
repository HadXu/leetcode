def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for i in nums:
        res ^= i
    return res

if __name__ == '__main__':
    nums = [1,2,3,2,3,1,4]
    res = singleNumber(nums)
    print(res)
