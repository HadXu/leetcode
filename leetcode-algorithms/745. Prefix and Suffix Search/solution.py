from typing import List
from collections import defaultdict

Trie = lambda: defaultdict(Trie)

class WordFilter:
	def __init__(self, words: List[str]):
		for weight, word in enumerate(words):
			word += '#'

			

	def f(self, prefix: str, suffix: str):
		pass


if __name__ == '__main__':
	words = []