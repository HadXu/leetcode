def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    from collections import Counter
    c = Counter(nums)
    return [k for k,_ in c.most_common(k)]


if __name__ == '__main__':
    res = topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(res)
