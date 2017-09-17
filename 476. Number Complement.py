def findComplement(num):
    """
    :type num: int
    :rtype: int
    """

    if num == 1:
        return 0
    if num == 0:
        return 1

    n = 0
    while 1<<n <= num:
        n += 1
    return (1<<n) -1 - num



if __name__ == '__main__':
    res = findComplement(0)
    print(res)