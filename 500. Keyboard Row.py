def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    up = set('qwertyuiopQWERTYUIOP')
    middle = set('asdfghjklASDFGHJKL')
    down = set('zxcvbnmZXCVBNM')
    return [w for w in words if set(w).issubset(up) or set(w).issubset(middle) or set(w).issubset(down)]






if __name__ == '__main__':
    res = findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(res)