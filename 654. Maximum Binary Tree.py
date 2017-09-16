class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    dummy = TreeNode(None)

    def d(root, nums):
        if not nums:
            return
        i = nums.index(max(nums))
        root.val = max(nums)
        if nums[:i]:
            root.left = TreeNode(None)
            d(root.left, nums[:i])
        if nums[i + 1:]:
            root.right = TreeNode(None)
            d(root.right, nums[i + 1:])

    d(dummy, nums)
    return dummy


if __name__ == '__main__':
   nums = [3,2,1,6,0,5]
   res = constructMaximumBinaryTree(nums)
   print(res.right.val)
   print(res.val)