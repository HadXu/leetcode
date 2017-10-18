def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    if num==0:
        return '0'
    s = []
    flag = False
    if num < 0:
        flag = True
        num = -num
    while num:
        s.append(str(num % 7))
        num //= 7
    if flag:
        s.append('-')
    s.reverse()
    return ''.join(s)


if __name__ == '__main__':
    num = 100
    res = convertToBase7(num)
    print(res)
