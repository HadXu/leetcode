class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.dfs(root, res)
        res = set(res)
        res = list(sorted(res))
        print(res)
        if len(res) <= 1:
            return -1
        return res[1]

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)
