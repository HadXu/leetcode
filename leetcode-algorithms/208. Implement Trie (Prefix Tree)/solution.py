from collections import defaultdict
from typing import List
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str) -> None:
        current = self.root
        for c in word:
            current = current.children[c]
        current.is_word = True


    def search(self, word:str) -> bool:
        current = self.root
        for c in word:
            current = current.children.get(c)
            if current is None:
                return False
        return current.is_word


    def startsWith(self, prefix:str) -> bool:
        current = self.root
        for c in prefix:
            current = current.children.get(c)
            if current is None:
                return False
        return True

    def enumerate(self, prefix:str) -> List:
        node = self.root
        word_list = []

        def dfs(node, word):
            if node.is_word:
                word_list.append(word)

            for a, n in node.children.items():
                dfs(n, word + a)

        tmp = ''
        for c in prefix:
            if not node.children.get(c):
                break

            tmp += c
            node = node.children[c]

        dfs(node, tmp)

        print(word_list)
        




if __name__ == '__main__':
    trie = Trie()
    for word in ["hello", "dog", "hell", "cat", "a",  "hel", "help", "helps", "helping"]:
        trie.insert(word)        

    res = trie.enumerate('a')







