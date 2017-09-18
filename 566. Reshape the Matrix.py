def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    import numpy as np
    try:
        return np.reshape(nums,(r,c)).tolist()
    except:
        return nums


if __name__ == '__main__':
    nums = [[1,2],
            [3,4]]
    r = 1
    c = 4
    res = matrixReshape(nums,r,c)
    print(res)



