class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def trimBST(root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """

    if not root:
        return root

    if root.val > R:
        return trimBST(root.left, L, R)
    if root.val < L:
        return trimBST(root.right, L, R)
    root.left = trimBST(root.left, L, R)
    root.right = trimBST(root.right, L, R)
    return root
