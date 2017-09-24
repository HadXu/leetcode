def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    if word.istitle() or word.islower() or word.isupper():
        return True
    return False


if __name__ == '__main__':
    s = ''
    res = detectCapitalUse(s)
    print(res)


