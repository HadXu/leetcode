def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    while num>9:
        tmp = 0
        while num:
            tmp += num % 10
            num //= 10
        num = tmp
    return num

if __name__ == '__main__':
    num = 38
    res = addDigits(num)
    print(res)


