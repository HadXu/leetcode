def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """

    from collections import Counter
    c = Counter(s)
    return ''.join([k*v for k,v in c.most_common()])

if __name__ == '__main__':
    s = 'abbca'
    res = frequencySort(s)
    print(res)


