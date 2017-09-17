def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    res = s.split(' ')

    return ' '.join([w[::-1] for w in res])

if __name__ == '__main__':
    res = reverseWords("Let's take LeetCode contest")
    print(res)