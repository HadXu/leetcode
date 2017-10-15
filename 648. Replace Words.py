def replaceWords(dict, sentence):
    """
    :type dict: List[str]
    :type sentence: str
    :rtype: str
    """

    rootset = set(dict)

    def replace(word):
        for i in range(1,len(word)):
            if word[:i] in rootset:
                return word[:i]
        return word
    return ' '.join(map(replace ,sentence.split()))


if __name__ == '__main__':
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    res = replaceWords(dict,sentence)
    print(res)