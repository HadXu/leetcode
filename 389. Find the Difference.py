def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    from functools import reduce
    from operator import xor
    return chr(reduce(xor,map(ord,s+t)))

if __name__ == '__main__':
    s = 'abcd'
    t = 'abcde'
    res = findTheDifference(s,t)
    print(res)