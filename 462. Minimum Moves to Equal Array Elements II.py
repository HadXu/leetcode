def minMoves2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    middle = sorted(nums)[len(nums)//2]

    return sum([abs(middle-v) for v in nums])


if __name__ == '__main__':
    nums = [1, 2, 3]
    res = minMoves2(nums)
    print(res)
