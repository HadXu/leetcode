def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    possible_sums = {0}
    for n in nums:
        possible_sums.update({(v + n) for v in possible_sums})

    return (sum(nums) / 2.) in possible_sums


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    res = canPartition(nums)
    print(res)
