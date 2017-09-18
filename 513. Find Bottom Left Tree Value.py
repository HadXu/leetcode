class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        info = []
        def dfs(node, depth=0):
            if node:
                if len(info) <= depth:
                    info.append([[],0])
                info[depth][0].append(node.val)
                info[depth][1] += 1
                dfs(node.left,depth+1)
                dfs(node.right,depth+1)
        dfs(root)
        return info[-1][0][0]

