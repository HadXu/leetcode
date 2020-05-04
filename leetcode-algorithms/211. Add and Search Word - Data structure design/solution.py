from typing import List
from collections import defaultdict
class WordDictionary:
	def __init__(self):
		self.root = {}

	def addWord(self, word:str) -> None:
		node = self.root
		for char in word:
			node = node.setdefault(char, {})
		node[None] = None


	def search(self, word:str) -> bool:
		def find(word, node):
			if not word:
				return None in node
			char, word = word[0], word[1:]
			if char != '.':
				return char in node and find(word, node[char])
			return any(find(word, kid) for kid in node.values() if kid)

		return find(word, self.root)

if __name__ == '__main__':
	wd = WordDictionary()
	wd.addWord('bad')
	wd.addWord('bull')
	wd.addWord('dad')
	wd.addWord('mad')

	print(wd.root)
	print(wd.search('b.'))

