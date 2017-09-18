def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """

    kinds = len(set(candies))
    res = min(len(candies)/2,kinds)
    return int(res)
if __name__ == '__main__':
    candies = [1,1,2,3]
    res = distributeCandies(candies)
    print(res)