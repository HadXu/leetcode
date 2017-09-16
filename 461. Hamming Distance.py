def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x^y).count('1')


if __name__ == '__main__':
    res = hammingDistance(2,4)
    print(res)