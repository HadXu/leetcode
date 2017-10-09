def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    p = 1
    res = []
    for i in nums:
        res.append(p)
        p *= i

    p = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] = res[i]*p
        p *= nums[i]
    return res


if __name__ == '__main__':
    nums = [1,2,3,4]
    res = productExceptSelf(nums)
    print(res)