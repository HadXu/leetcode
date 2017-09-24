# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        from collections import Counter
        c = Counter()
        def getsum(node):
            if not node:
                return 0
            s = node.val+getsum(node.left)+getsum(node.right)
            c[s]+=1
            return s
        getsum(root)
        freq = max(c.values())
        return [s for s in c.keys() if c[s]==freq]
