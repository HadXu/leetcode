def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    # return [bin(n).count('1') for n in range(num+1)]

    res = [0]
    for i in range(1, num + 1):
        res.append(res[i >> 1] + (i & 1))
    return res


if __name__ == '__main__':
    res = countBits(5)
    print(res)
