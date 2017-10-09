def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    return '00' not in bin(n) and '11' not in bin(n)


if __name__ == '__main__':
    res = hasAlternatingBits(5)
    print(res)
