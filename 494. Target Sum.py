def findTargetSumWays(nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """

    dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}

    for i in range(1, len(nums)):
        tdic = {}
        for d in dic:
            tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
            tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)

        dic = tdic

    return dic.get(S, 0)


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    S = 3

    res = findTargetSumWays(nums, S)
    print(res)
