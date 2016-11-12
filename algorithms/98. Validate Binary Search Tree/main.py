# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def to_list(root):
            if not root:
                return []
            else:
                mid = root.val
                left_list = to_list(root.left)
                right_list = to_list(root.right)
                return left_list + [mid] + right_list
        lst = to_list(root)
        for pre, next in zip(lst[:-1], lst[1:]):
            if pre >= next:
                return False
        return True
