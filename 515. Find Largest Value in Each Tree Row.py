class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def largestValues(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    info = []

    def dfs(node, depth=0):
        if node:
            if len(info) <= depth:
                info.append([float('-inf'), 0])
            info[depth][0] = max(info[depth][0], node.val)
            info[depth][1] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

    dfs(root)
    return [v[0] for v in info]
