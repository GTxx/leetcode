# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        else:
            left_invert = self.invertTree(root.left)
            right_invert = self.invertTree(root.right)
            root.left = right_invert
            root.right = left_invert
            return root

