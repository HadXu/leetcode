class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#### 中序遍历即可 得到有序的，此时采用队列即可
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        from collections import deque
        self.d = deque()
        self.InOrder(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.d

    def next(self):
        """
        :rtype: int
        """
        item = self.d.pop()
        return item



    def InOrder(self,node):
        if node:
            self.InOrder(node.left)
            self.d.appendleft(node.val)
            self.InOrder(node.right)



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
