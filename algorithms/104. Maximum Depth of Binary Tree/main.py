# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            if not root.left and not root.right:
                return 1
            else:
                left_max_depth = self.maxDepth(root.left)
                right_max_depth = self.maxDepth(root.right)
                return 1 + max(left_max_depth, right_max_depth)


