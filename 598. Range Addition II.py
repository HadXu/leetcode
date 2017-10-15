def maxCount(m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    if not ops:
        return m*n
    return min(op[0] for op in ops) * min(op[1] for op in ops)

if __name__ == '__main__':
    ops = [[2, 2], [3, 3]]
    res = maxCount(3, 3, ops)
    print(res)
