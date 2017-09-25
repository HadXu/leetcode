def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """

    """
    int getSum(int a, int b) {
        return b==0?a:getSum(a^b,(a&b)<<1);
    }
    """


    MAX_INT = 0x7FFFFFFF
    MIN_INT = 0x80000000
    MASK = 0x100000000

    while b:
        a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
    return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


if __name__ == '__main__':
    a, b = -1, 1
    res = getSum(a, b)
    print(res)
