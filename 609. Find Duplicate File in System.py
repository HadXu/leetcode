def findDuplicate(paths):
    """
    :type paths: List[str]
    :rtype: List[List[str]]
    """
    from collections import defaultdict
    M = defaultdict(list)
    for item in paths:
        data = item.split(' ')
        root = data[0]
        for file in data[1:]:
            name,_,context = file.partition('(')
            M[context[:-1]].append(root+'/'+name)
    return [v for v in M.values() if len(v)>1]





if __name__ == '__main__':
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    res = findDuplicate(paths)
    print(res)