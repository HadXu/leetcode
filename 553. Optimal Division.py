def optimalDivision(nums):
    """
    :type nums: List[int]
    :rtype: str
    """

    A = list(map(str, nums))
    if len(nums) <= 2:
        return '/'.join(A)
    return '{}/({})'.format(A[0], '/'.join(A[1:]))


if __name__ == '__main__':
    nums = [1000, 100, 10, 2]
    res = optimalDivision(nums)
    print(res)
