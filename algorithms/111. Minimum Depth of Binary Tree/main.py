# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            left_min_path = self.minDepth(root.left)
            right_min_path = self.minDepth(root.right)
            if left_min_path == 0:
                return right_min_path + 1
            if right_min_path == 0:
                return left_min_path + 1
            return min(left_min_path, right_min_path) + 1
