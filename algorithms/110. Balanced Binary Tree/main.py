# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _is_balance(root):
            if not root:
                return True, 0
            else:
                left_balance, left_height = _is_balance(root.left)
                if not left_balance:
                    return False, 0

                right_balance, right_height = _is_balance(root.right)
                if not right_balance:
                    return False, 0

                if abs(right_height - left_height) <= 1:
                    return True, max(left_height, right_height) + 1
                else:
                    return False, 0
        return _is_balance(root)[0]
