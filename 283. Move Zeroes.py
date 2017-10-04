def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    index = 0
    for i in nums:
        if i != 0:
            nums[index] = i
            index += 1
    while index < len(nums):
        nums[index] = 0
        index += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)
