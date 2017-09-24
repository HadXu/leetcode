def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    s = set()
    for i in nums:
        if i not in s:
            s.add(i)
        else:
            s.discard(i)
    return list(s)


if __name__ == '__main__':
    nums = [1,2,1,3,2,5]
    res = singleNumber(nums)
    print(res)
