class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = []

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.dict = dict

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        def distence(str1,str2):
            count = 0
            for x,y in zip(str1,str2):
                if x!=y:
                    count += 1
            return count == 1

        for w in self.dict:
            if len(w)==len(word) and distence(w,word):
                return True
        return False

if __name__ == '__main__':
    obj = MagicDictionary()
    dict = ["hello", "leetcode"]
    obj.buildDict(dict)
    param_2 = obj.search('hhllo')
    print(param_2)




