def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for x in nums:
        if nums[abs(x) - 1] < 0:
            res.append(abs(x))
        else:
            nums[abs(x) - 1] *= -1
    return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    res = findDuplicates(nums)
    print(res)
