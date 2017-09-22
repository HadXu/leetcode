def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    res = 0
    cnt = 0
    for i in nums:
        if i==1:
            cnt += 1
            res = max(res,cnt)
        else:
            cnt = 0
    return res

if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    res = findMaxConsecutiveOnes(nums)
    print(res)
