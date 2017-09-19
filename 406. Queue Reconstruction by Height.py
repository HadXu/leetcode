def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """

    people.sort(key=lambda p: (-p[0], p[1]))
    queue = []
    for p in people:
        queue.insert(p[1],p)
    return queue


if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    res = reconstructQueue(people)
    print(res)
